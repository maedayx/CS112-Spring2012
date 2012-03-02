#! /usr/bin/env python

import pygame
from pygame.locals import *

# Globals
BACKGROUND = 80, 80, 80
RED = 255,0,0
WHITE = 255,255,255
GREEN = 0,255,0
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
RECT_SIZE = 120, 80

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

bounds = screen.get_rect()
rects = [pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE) ]

rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

bigFont = pygame.font.Font(None, 80)

grabbed = None

done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect
            if grabbed:
                rects.remove(grabbed)
                rects.append(grabbed)
        elif evt.type == MOUSEBUTTONUP:
            grabbed = None
    
    # Draw
    screen.fill(BACKGROUND)
    text = bigFont.render("Drag the rectangles", True, (0,0,0), BACKGROUND)
    loc = text.get_rect()
    loc.center = bounds.center
    screen.blit(text, loc)
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)
    
    for rect in rects:
        others = rects[:]
        others.remove(rect)
        if rect == grabbed:
            color = WHITE
        elif rect.collidelist(others) != -1:
            color = GREEN
        else:
            color = RED
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 5)
    
    # Refresh
    pygame.display.flip()
    clock.tick(FPS)