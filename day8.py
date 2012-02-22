#! /usr/bin/env python

from random import randint
import pygame
from pygame import draw
from pygame.locals import *

# Initliazation
pygame.init()
screen = pygame.display.set_mode((800,600))

# Draw tie fighter function
def tieFighter (pos, screen, color, height=40):
    x, y = pos
    width = height/8
    draw.rect(screen, color, (x, y, width, height))
    draw.rect(screen, color, (x+height-width, y, width, height))
    draw.rect(screen, color, (x, y+(height-width)/2, height, width))
    draw.circle(screen, color, (x+height/2, y+height/2), height/4)

# Setup the screen
screen.fill((0,0,0))

# Setup the game loop
done = False
col = 0
change = 1
x = 50
y = 50
pygame.key.set_repeat(100,100)
color = []
pos = []
size = []
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            y -= 5
        elif event.type == KEYDOWN and event.key == K_DOWN:
            y += 5
        elif event.type == KEYDOWN and event.key == K_LEFT:
            x -= 5
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            x += 5
        elif event.type == MOUSEBUTTONDOWN:
            color.append((col,0,col))
            pos.append(pygame.mouse.get_pos())
            size.append(randint(20,80))
   
    # Draw LOTS OF tie fighters
    col += change
    if col > 255 or col < 0:
        change *= -1
        col += change
        
    screen.fill((0,0,0))
    
    for i in range(len(color)-1,-1,-1):
        size[i] -= 1
        if size[i] <= 0:
            size.pop(i)
            color.pop(i)
            pos.pop(i)
        else:
            tieFighter(pos[i], screen, color[i], size[i])
    
    pygame.display.flip()
    clock.tick(15)