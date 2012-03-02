#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.

"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      
def find_coins(room):
    coins = []
    for x,row in enumerate(room):
        for y,loc in enumerate(row):
            if loc == 1:
                coins.append((y,x))
    return coins


# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player
import math
def distance_from_player(player_x, player_y, width, height):
    "calculates the distance of each square from the player"
    xTerm = 0.0
    yTerm = 0.0
    dist = 0.0
    room = [ [0 for i in range(width)] for i in range(height) ]
    for x,row in enumerate(room):
        for y,loc in enumerate(row):
            xTerm = (x-player_x)**2
            yTerm = (y-player_y)**2
            dist = math.sqrt(xTerm + yTerm)
            room[x][y] = dist
    
    return room
