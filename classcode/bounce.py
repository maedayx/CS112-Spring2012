import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

tie_x, tie_y = 400,300
ties = []
color = []

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)

def moveTie(x, y, dx, dy, bounds, size):
    if dx > 100:
        dx = 1
    elif dx < -100
        dx = -1
    if dy > 100:
       dy = 1
    elif dy < -100
       dy = -1
    if x >= bounds.right-size or x <= bounds.left:
        if dx > 0:
            dx += 1
        else:
             dx -= 1
        dx *= -1
    if y >= bounds.bottom-size or y <= bounds.top:
        if dy > 0:
            dy += 1
        else:
             dy -= 1
        dy *= -1
    return x+dx, y+dy, dx, dy

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()
tie_dx = 3
tie_dy = 3
tie_size = 40
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))
    tie_x, tie_y, tie_dx, tie_dy = moveTie(tie_x, tie_y, tie_dx, tie_dy, screen_bounds, tie_size)
    ties.append([tie_x, tie_y])
    if len(ties) > 50:
        ties.pop(0)
    for i in range(len(ties)):
        draw_tie(screen, ties[i], (i*5,i*3,0))
        
    #draw_tie(screen, [tie_x, tie_y], size = tie_size)
    
    pygame.display.flip()
    clock.tick(60)
    
print "ByeBye"