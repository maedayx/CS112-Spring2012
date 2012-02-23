#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    if pt[0] >= box[0] and pt[0] <= box[0]+box[2]-1 and pt[1] >= box[2] and pt[1] <= box[1]+box[3]-1:
        return True;
    else:
        return False;