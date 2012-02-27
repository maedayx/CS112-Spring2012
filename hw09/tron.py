#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *
from pygame import draw

# Function to draw a player
def drawPlayer (pos, screen, color):
    x, y = pos
    draw.rect(screen, color, (x, y, 5, 5))
    
# Initialization
pygame.init()
screen = pygame.display.set_mode((800,600))

# Set up some constants
RED = 255,0,0
BLUE = 0,0,255
WHITE = 255,255,255
GREEN = 0,255,0

# Set up player variables
# player 1
player1 = {'x':200, 'y':300, 'xDir':1, 'yDir':0}
player1Trail = []
# player 2
player2 = {'x':600, 'y':300, 'xDir':-1, 'yDir':0}
player2Trail = []

# Setup the screen
screen.fill((0,0,0))

# Game Loop
done = False
winner = None
playing = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        # Game Loop control
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            if not winner:
                playing = True
            else:
                screen.fill((0,0,0))
                player1 = {'x':200, 'y':300, 'xDir':1, 'yDir':0}
                player1Trail = []
                player2 = {'x':600, 'y':300, 'xDir':-1, 'yDir':0}
                player2Trail = []
                winner = None
        # Player 1 Movement
        elif event.type == KEYDOWN and event.key == K_UP:
            # Make sure you can't reverse direction
            if player1['yDir'] == 0:
                player1['yDir'] = -1
                player1['xDir'] = 0
        elif event.type == KEYDOWN and event.key == K_DOWN:
            # Make sure you can't reverse direction
            if player1['yDir'] == 0:
                player1['yDir'] = 1
                player1['xDir'] = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            # Make sure you can't reverse direction
            if player1['xDir'] == 0:
                player1['yDir'] = 0
                player1['xDir'] = -1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            # Make sure you can't reverse direction
            if player1['xDir'] == 0:
                player1['yDir'] = 0
                player1['xDir'] = 1
        # Player 2 Movement
        elif event.type == KEYDOWN and event.key == K_w:
            # Make sure you can't reverse direction
            if player2['yDir'] == 0:
                player2['yDir'] = -1
                player2['xDir'] = 0
        elif event.type == KEYDOWN and event.key == K_s:
            # Make sure you can't reverse direction
            if player2['yDir'] == 0:
                player2['yDir'] = 1
                player2['xDir'] = 0
        elif event.type == KEYDOWN and event.key == K_a:
            # Make sure you can't reverse direction
            if player2['xDir'] == 0:
                player2['yDir'] = 0
                player2['xDir'] = -1
        elif event.type == KEYDOWN and event.key == K_d:
            # Make sure you can't reverse direction
            if player2['xDir'] == 0:
                player2['yDir'] = 0
                player2['xDir'] = 1
    
    if playing:
        # Move player 1 and add to it's trail
        player1Trail.append((player1['x'],player1['y']))
        player1['x'] += player1['xDir']
        player1['y'] += player1['yDir']
        # Move player 2 and add to it's trail
        player2Trail.append((player2['x'],player2['y']))
        player2['x'] += player2['xDir']
        player2['y'] += player2['yDir']
    
    # Draw player 1
    drawPlayer((player1['x'],player1['y']), screen, RED)
    # Draw player 2
    drawPlayer((player2['x'],player2['y']), screen, BLUE)
    
    # Check for collisions on player 1's trail
    for i in range(len(player1Trail)-1):
           # Check to see if player 1 collided with it's own trail
        if player1Trail[i] == (player1['x'],player1['y']):
            playing = False
            winner = 2
        # Check to see if player 2 collided with player 1's trail
        if player1Trail[i] == (player2['x'],player2['y']):
            playing = False
            winner = 1
    # Check for collisions on player 2's trail         
    for i in range(len(player2Trail)-1):
        # Check to see if player 2 collided with it's own trail
        if player2Trail[i] == (player2['x'],player2['y']):
            playing = False
            winner = 1
        # Check to see if player 1 collided with player 2's trail
        if player2Trail[i] == (player1['x'],player1['y']):
            playing = False
            winner = 2
        
    # Check to see if someone goes off the screen
    if player1['x'] >= 800 or player1['x'] <= 0 or player1['y'] >= 600 or player1['y'] <= 0:
        playing = False
        winner = 2
    if player2['x'] >= 800 or player2['x'] <= 0 or player2['y'] >= 600 or player2['y'] <= 0:
        playing = False
        winner = 1
    
    if winner == 1:
        drawPlayer((player1['x'],player1['y']), screen, GREEN)
        drawPlayer((player2['x'],player2['y']), screen, WHITE)
    elif winner == 2:
        drawPlayer((player2['x'],player2['y']), screen, GREEN)
        drawPlayer((player1['x'],player1['y']), screen, WHITE)

    pygame.display.flip()
    clock.tick(60)