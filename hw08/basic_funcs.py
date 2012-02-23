#!/usr/bin/env python
import sys
# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name);
    print "hello,", name.lower();


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    if w is '' or h is '':
        print "Error: Invalid Dimensions"
        return
    
    w = float(w)
    h = float(h)
    
    if h%1 != 0 or w%1 != 0:
        print "Error: Invalid Dimensions"
        return
    
    if not h or not w:
        print "Error: Invalid Dimensions"
        return
    if h <= 0 or w <= 0:
        print "Error: Invalid Dimensions"
        return
        
    w = int(w)
    h = int(h)    
    
    if w > 2 and h > 1:
        # Build top line
        box = "+"
        for x in range(w-2):
            box += "-"
        box += "+\n"

        # Build middle section
        for y in range(h-2):
            box += "|"
            for x in range(w-2):
                box += " "
            box += "|\n"

        # Build bottom line
        box += "+"
        for x in range(w-2):
            box += "-"
        box += "+"
    elif w == 2:
        box = "++"
    else:
        box = "+"

    print box
    


# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

