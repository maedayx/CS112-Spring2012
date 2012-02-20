#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

# Get numbers from user
nums = input_nums()

#Output them
print "Before sort:"
print nums

# Find the range to use for sorting
theRange = len(nums)-1

# Sorting loop
for x in range(theRange):
    # Assume we're at the minimum
    minimum = x
    # Go through the rest of list and see if we find anything smaller than our current proposed minimum
    for i in range(x+1, theRange):
        if nums[i] < nums[minimum]:
            minimum = i
    # If we found a smaller number later in the list, swap 'em and start over
    if minimum != x:
        nums[x],nums[minimum] = nums[minimum],nums[x]

# Output the sorted list
print "After sort:"
print nums
