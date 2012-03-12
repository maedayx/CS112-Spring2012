#! /usr/bin/env python

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group
from random import randrange, randint

from guns import *

# Basic ship, used for player and enemies
class Ship (Sprite):   
    width = 10
    height = 10
    bullet_type = Bullet
    shoot_freq = 50
    
    def __init__(self, x, y, vx, vy, bounds, bullet_group, color=''):
        Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.bounds = bounds
        if color:
            self.color = color
        self.bullet_group = bullet_group
        
        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()
    
    def draw_image(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = 0
            self.rect.x += -2 * dx

        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = 0
            self.rect.y += -2 * dy
        
        
    def shoot(self, vel, bad):
        bullet = self.bullet_type(self.rect.x, self.rect.y, vel, (255,255,255), self.bounds, bad = bad)
        self.bullet_group.add(bullet)
        
    def die(self):
        self.kill()

# Generic spawner class
class Spawner(object):
    ship_type = Ship
    xmax = 780
    ymax = 600
    color = ''
    def __init__(self, frequency, ship_group, bounds, bullet_group):
        self.frequency = frequency
        self.bounds = bounds
        self.bullet_group = bullet_group
        self.ship_group = ship_group
            
    def random_spawn(self):
        if randint(self.frequency) == 0:
            x = randrange(self.xmax)
            y = randrange(self.ymax)
            if self.color:
                ship = self.ship_type(x, y, 50, 50, self.bounds, self.bullet_group, self.color)
            else:
                ship = self.ship_type(x, y, 50, 50, self.bounds, self.bullet_group)
            self.ship_group.add(ship)
