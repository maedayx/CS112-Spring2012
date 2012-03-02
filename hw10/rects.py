#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""
import pygame
from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    isInside = True
    for point in poly:
        if not rect.collidepoint(point):
            isInside = False
    return isInside


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    "create a rectangle which surounds a polygon"
    xMin = xMax = yMin = yMax = None
    # There's gotta be a better way to do this, but we're finding the minimum and maximum x and y dimensions of the polygon.
    for point in poly:
        if xMin == None:
            xMin = point[0]
        elif point[0] < xMin:
            xMin = point[0]
        
        if xMax == None:
            xMax = point[0]
        elif point[0] > xMax:
            xMax = point[0]
        
        if yMin == None:
            yMin = point[1]
        elif point[1] < yMin:
            yMin = point[1]
        
        if yMax == None:
            yMax = point[1]
        elif point[1] > yMax:
            yMax = point[1]
            
    if yMin < 0:
        yMax += abs(yMin)+1
    else:
        yMax += yMin
            
    rect = pygame.Rect(xMin, yMin, xMax, yMax)      
    return rect
