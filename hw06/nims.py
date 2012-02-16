#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
# This function will prompt the user for an integer in a given range, make sure it's within the range, and return the integer.
def getInt(start='0', end='9999', msg='Enter an integer.', prompt='>>> '):
    numIn = None
    while numIn > end or numIn < start:
        print msg
        numIn = raw_input(prompt)
        try:
            numIn = int(numIn)
        except ValueError:
            print "Please enter a valid integer between {0} and {1}".format(start, end)
            numIn = None
        if numIn > end or numIn < start:
            print "Please enter a valid integer between {0} and {1}".format(start, end)
    return numIn
        
            

stones = 0
perTurn = 0

# Get game settings from user.
stones = getInt(start=0, msg="How many stones would you like to play with?")
perTurn = getInt(start=0, end=stones, msg="What should the maximum number of stones per turn be?")

# Main game loop
while stones > 0:
    # Player 1's turn
    print "{0} stones left.".format(stones)
    thisTurn = getInt(start=1, end=stones, msg='Player 1, how many stones would you like to take? [1 - {0}]'.format(perTurn))
    stones -= thisTurn
    if stones == 0:
        print "No stones left!"
        print "Player 2 wins!"
        break;
    # Player 2's turn
    print "{0} stones left.".format(stones)
    thisTurn = getInt(start=1, end=stones, msg='Player 2, how many stones would you like to take? [1 - {0}]'.format(perTurn))
    stones -= thisTurn
    if stones == 0:
        print "No stones left!"
        print "Player 1 wins!"
        break;
