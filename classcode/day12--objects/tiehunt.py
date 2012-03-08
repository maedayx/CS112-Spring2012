#!/usr/bin/env python

import math

from random import randrange
import random

import pygame
from pygame.locals import *


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)

class TieFighter(object):
    def __init__(self, x, y, vx, vy, bounds, size=40, color=C_RED):
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color
        self.bounds = bounds
        
        self.image = pygame.Surface((size,size))
        draw_tie(self.image, color, size)
        
        self.rect = pygame.Rect(x, y, size, size)
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx *= -1
            self.rect.x += self.vx*2
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy *= -1
            self.rect.y += self.vy*2
        

class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)
        self.ties = []
        self.ties.append(TieFighter(200, 200, 3, 3, self.bounds))
    
    def spawn(self):
        x = random.randint(1,self.size[0]-1)
        y = random.randint(1,self.size[1]-1)
        vx = random.randint(1,6)
        vy = random.randint(1,6)
        self.ties.append(TieFighter(x, y, vx, vy, self.bounds))

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            # update
            self.spawn()
            for tie in self.ties:
                tie.update()

            # draw
            self.screen.fill(C_BLACK)
            
            for tie in self.ties:
                tie.draw(self.screen)
            
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
