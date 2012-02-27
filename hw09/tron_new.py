#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *
from pygame import draw

# Player class
class Player:
    def __init__(self, loc, xDir, color):
        self.x, self.y = loc
        self.xDir = xDir
        self.yDir = 0
        self.trail = []
        self.color = color
    def changeDir(self, x = 0, y = 0):
        self.xDir = x
        self.yDir = y
    def move(self):
        self.trail.append((self.x,self.y)) # Add the the list of places the player has been
        self.x += self.xDir
        self.y += self.yDir
    def draw(self, screen):
        draw.rect(screen, self.color, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
    def update(self, screen):
        # This method simply does move and draw in one call, to make the game loop tidier.
        self.move()
        self.draw(screen)
    def checkCollision(self, loc):
        # This method checks to see if loc is in the list of places the player has been, and returns True if it is.
        if loc in self.trail:
            return True
        else:
            return False       

# Set up some constants
PLAYER1_COLOR = 255,0,0
PLAYER2_COLOR = 0,0,255
LOSER_COLOR = 255,255,255
WINNER_COLOR = 0,255,0
PLAYER_SIZE = 5
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER1_START = SCREEN_WIDTH/4, SCREEN_HEIGHT/2
PLAYER2_START = (SCREEN_WIDTH/4)+SCREEN_WIDTH/2, SCREEN_HEIGHT/2

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# Setup the screen
screen.fill((0,0,0))

# Initliaze the players
players = [Player(PLAYER1_START, 1, PLAYER1_COLOR), Player(PLAYER2_START, -1, PLAYER2_COLOR)]


# Set up some game control variables
done = False
winner = None
playing = False
losers = []
clock = pygame.time.Clock()

# Draw the players in their starting spots
for player in players:
    player.draw(screen)

# Start the game loop
while not done:
    for event in pygame.event.get():
        # Game Loop control
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            # If the game is set up, start it
            if not winner:
                playing = True
            # Otherwise, reset the game
            else:
                screen.fill((0,0,0)) # Clear the screen
                winner = None # Reset game control variables
                losers = []
                players = [Player(PLAYER1_START, 1, PLAYER1_COLOR), Player(PLAYER2_START, -1, PLAYER2_COLOR)] # Reinitialize the players
                # Draw the players in their starting spots
                for player in players:
                    player.draw(screen)
        
        # Player 1 Movement
        elif event.type == KEYDOWN and event.key == K_UP:
            # Make sure you can't reverse direction
            if players[0].yDir == 0:
                players[0].changeDir(y = -1)
        elif event.type == KEYDOWN and event.key == K_DOWN:
            # Make sure you can't reverse direction
            if players[0].yDir == 0:
                players[0].changeDir(y = 1)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            # Make sure you can't reverse direction
            if players[0].xDir == 0:
                players[0].changeDir(x = -1)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            # Make sure you can't reverse direction
            if players[0].xDir == 0:
                players[0].changeDir(x = 1)
        
        # Player 2 Movement
        elif event.type == KEYDOWN and event.key == K_w:
            # Make sure you can't reverse direction
            if players[1].yDir == 0:
                players[1].changeDir(y = -1)
        elif event.type == KEYDOWN and event.key == K_s:
            # Make sure you can't reverse direction
            if players[1].yDir == 0:
                players[1].changeDir(y = 1)
        elif event.type == KEYDOWN and event.key == K_a:
            # Make sure you can't reverse direction
            if players[1].xDir == 0:
                players[1].changeDir(x = -1)
        elif event.type == KEYDOWN and event.key == K_d:
            # Make sure you can't reverse direction
            if players[1].xDir == 0:
                players[1].changeDir(x = 1)
    
    if playing:
        # Check for losing conditions
        for currPlayer in players:
            # Did the player go off the screen?
            if currPlayer.x >= SCREEN_WIDTH or currPlayer.x <= 0 or currPlayer.y >= SCREEN_HEIGHT or currPlayer.y <= 0:
                losers.append(currPlayer)
            # Did anyone hit a trail?
            for checkPlayer in players:
                if currPlayer.checkCollision((checkPlayer.x, checkPlayer.y)):
                   losers.append(checkPlayer)
            # Move the player and add to it's trail
            currPlayer.update(screen)
    
    # If there's only one player left who's not a loser, stop the game, and mark that player as the winner
    if len(losers) == len(players)-1:
        playing = False
        for player in players:
            if player not in losers:
                winner = player
    
    # If we have a winner, draw that player in green and all the losers in white
    if winner:
        winner.color = WINNER_COLOR
        winner.draw(screen)
        for loser in losers:
            loser.color = LOSER_COLOR
            loser.draw(screen)

    # Refresh
    pygame.display.flip()
    clock.tick(60)