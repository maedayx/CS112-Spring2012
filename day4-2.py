#! /usr/bin/env python

import pygame
from pygame.locals import *

# Settings
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255
GREEN = 0,255,0
size = 400,400

# initialize
pygame.init()
screen = pygame.display.set_mode(size)

done = False
sep = 8
pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            sep += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            if sep > 1:
                sep-= 1
    ## Draw ##
    screen.fill(BLACK)
    for i in range(0,400,sep):
        pygame.draw.line(screen,RED,(0,i),(i,399))
        pygame.draw.line(screen,BLUE,(i,0),(399,i))
        pygame.draw.line(screen,GREEN,(399,i),(399-i,399))
        pygame.draw.line(screen,GREEN,(399-i,0),(0,i))
        
    
    pygame.display.flip()