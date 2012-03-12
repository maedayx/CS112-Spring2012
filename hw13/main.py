#!/usr/bin/env python
"""
SQWARS: A Graphics-Lite Shmup!

TODO:
    - Be able to restart the game
    - Add bombs that randomly spawn, if a player grabs one, all the enemies die!
    - Add the RadGuy enemy: Changes colors and warps around the screen. Very rare. If it touches the player, the player loses a life!
    - Comment code!
"""

import math
from random import randrange

import pygame
from pygame import Rect, Surface, draw
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from ships import *
from ui import UpdateText, InfoText

# Set up some constants
BADGUY_COLOR = 255, 0, 255
FASTGUY_COLOR = 255, 255, 0
MADGUY_COLOR = 255, 0, 0
PLAYER_COLOR = 0, 255, 0
PLAYER_LIVES = 1
LOSE_LIFE_COLOR = 255, 0, 0
BOTTOM = 400

# This is the basic enemy
class BadGuy(Ship):
    color = BADGUY_COLOR
    bullet_type = Bullet
    width = 20
    height = 20
    speed = 100
    def __init__(self, x, y, direction, bounds, bullet_group, color=''):
        Ship.__init__(self, x, y, direction, 0, bounds, bullet_group, color)
        self.vx = self.speed * self.vx # Vx is used as a direction here, rather than a direction and velocity
        
    def update(self, dt):
        # Move
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy
        
        # If it touches the edge of the screen, it moves down and reverses x direction
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.y += self.height * 2
            self.rect.x += -2 * dx   
        
        # Shoot at random times
        if randrange(self.shoot_freq) == 0:
            self.shoot(self.speed, True)

# Just like BadGuy except it moves faster and shoots less            
class FastGuy(BadGuy):
    color = FASTGUY_COLOR
    speed = 300
    shoot_freq = 100

# Just like BadGuy except it moves slower and shoots more        
class MadGuy(BadGuy):
    color = MADGUY_COLOR
    speed = 50
    shoot_freq = 25
            
# The Player!
class Player(Ship):
    color = PLAYER_COLOR
    lives = PLAYER_LIVES
    last_hit = 0
    do_count = False
    
    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)
        
    def update(self, dt):
        # Move
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy
        self.atedge = None
        
        # Don't let it go off the screen! (It only moves side to side)
        if self.rect.left < self.bounds.left:
            self.vx = 0
            self.atedge = "Left"
        if self.rect.right > self.bounds.right:
            self.vx = 0
            self.atedge = "Right"
        
        # If the player is currently red (from getting hit), check how long it's been red for and change back to green if it's been long enough
        if self.do_count:
            self.last_hit += 1
            if self.last_hit > 6:
                self.color = PLAYER_COLOR
                self.last_hit = 0
                self.do_count = False
        
    def shoot(self, vel):
        vel *= -1 # Since the player's bullets shoot UP we have to reverse the velocity
        Ship.shoot(self, vel, False)
        
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            self.color = LOSE_LIFE_COLOR
            self.last_hit = 0
            self.do_count = True

# This makes it so that the player can only ever have a limited number of bullets onscreen
class BulletGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
        self.count = count
        
    def add(self, *sprites):
        for sprite in sprites:
            if len(self) < self.count:
                Group.add(self, sprite)
 
# Spawns bad guys at random spots with random frequency (within a range)               
class BadGuySpawner(Spawner):
    ship_type = BadGuy
    xmax = 780 # This should be changed to NOT be a magic number.
    ymax = BOTTOM

    def random_spawn(self):
        if randrange(self.frequency) == 0:
            x = randrange(self.xmax)
            y = randrange(self.ymax)
            if self.color:
                ship = self.ship_type(x, y, -1, self.bounds, self.bullet_group, self.color)
            else:
                ship = self.ship_type(x, y, -1, self.bounds, self.bullet_group)
            self.ship_group.add(ship)

# Same as above but spawns FastGuys
class FastGuySpawner(BadGuySpawner):
    ship_type = FastGuy

# Same as above but spawns MadGuys
class MadGuySpawner(BadGuySpawner):
    ship_type = MadGuy

class Game(Application):
    title = "Sqwars"
    screen_size = 800, 600
    min_dt = 200
    pause_key = K_p
    paused_text = "Press P to blast more baddies!"
    gameover_msg = "Game Over!"
        
    def __init__(self):
        Application.__init__(self)
        pygame.key.set_repeat(100,100)
        
        self.gameover = False
        self.kills = 0
        
        self.ships = Group()
        self.bullets = Group()
        self.player_bullets = BulletGroup(10)
        self.spawners = [   BadGuySpawner(100, self.ships, self.bounds, self.bullets),
                            FastGuySpawner(250, self.ships, self.bounds, self.bullets),
                            MadGuySpawner(300, self.ships, self.bounds, self.bullets)]
        
        self.player = Player(self.screen_size[0]/2, self.screen_size[1]-25, 0, 0, self.bounds, self.player_bullets)
                
        self.killed_text = UpdateText("Killed: ", self.kills, (self.screen_size[0]-100, self.screen_size[1]-25), 30)
        self.lives_text = UpdateText("Lives: ", self.player.lives, (10, self.screen_size[1]-25), 30)
            
    def handle_event(self, event):
        self.player.vx = 0 # Player only moves when the key is down
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.shoot(200)
        if key[pygame.K_LEFT] and self.player.atedge != "Left":
            self.player.vx = -150
        if key[pygame.K_RIGHT] and self.player.atedge != "Right":
            self.player.vx = 150
    
    def update(self):
        dt = min(self.min_dt, self.clock.get_time())
        self.bullets.update(dt)
        self.player_bullets.update(dt)
        
        # Check if any of the enemy bullets hit the player, if they did, the player loses a life
        if pygame.sprite.spritecollide(self.player, self.bullets, True):
            self.player.lose_life()
            self.lives_text.var = self.player.lives
        
        # Check if any of the player bullets hit an enemy, if they did, kill the enemy and give the player more points
        for bullet in self.player_bullets:
            self.kills += bullet.kill_things(self.ships, self.player)
            self.killed_text.var = self.kills
        
        # Check if any of the player's bullets hit a enemy bullet, if they did, they both disappear    
        pygame.sprite.groupcollide(self.player_bullets, self.bullets, True, True)
        
        
        self.ships.update(dt)
        self.player.update(dt)
        
        for spawner in self.spawners:
            spawner.random_spawn()
        
        # If ships get by the player, the player loses a life!
        for ship in self.ships:
            if ship.rect.bottom > self.bounds.bottom:
                ship.kill()
                self.player.lives -= 1
                
        if self.player.lives == 0:
            self.do_gameover()
    
    def draw(self, screen):
        # Draw E'ERTHANG
        screen.fill((0,0,0))
        self.ships.draw(screen)
        self.bullets.draw(screen)
        self.player_bullets.draw(screen)
        self.player.draw(screen)
        self.killed_text.draw(screen)
        self.lives_text.draw(screen)

if __name__ == "__main__":
    Game().run()
    print "ByeBye"
