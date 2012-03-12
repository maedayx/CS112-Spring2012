#! /usr/bin/env python

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

# This is the gun that everything uses (for now)
class Bullet(Sprite):
    width = 5
    height = 5
    
    def __init__(self, x, y, vy, color, bounds, bad=True):
        Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.bounds = bounds
        self.bad = bad
        
        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()
        
    def draw_image(self):
        self.image.fill(self.color)
        
    def update(self, dt):
        dt /= 1000.0
        dy = int(self.vy * dt)
        self.rect.y += dy
        
        # We don't want to keep track of them once they're off the screen, so get rid of them
        if self.rect.bottom > self.bounds.bottom or self.rect.top < self.bounds.top:
            self.kill()
            
    # only used for player bullets (separate class?), checks to see if it hit any enemies, if it did kill the enemy and return a point for the player
    def kill_things(self, ships, player):
        kills = 0
        for ship in ships:
            if self.rect.colliderect(ship.rect) and not self.bad:
                ship.die()
                kills += 1
            
        return kills
    
        