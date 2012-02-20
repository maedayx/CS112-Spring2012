#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

# Get a list of numbers from the user and sort them
nums = input_nums()
nums = sorted(nums)
print nums
print "I have sorted your numbers"

# Ask the user for a number to find
searchFor = raw_input("Which number should I find: ")
searchFor = int(searchFor)

# Set our starting range
minimum = 0
maximum = len(nums)-1

# Search loop
while maximum >= minimum:
    # This is where in the array we're looking
    mid = maximum+minimum/2
    if nums[mid] == searchFor:
        break # If the number matches the one we're looking for, good! End the loop
    elif searchFor > nums[mid]:
        minimum = mid+1 # Otherwise, if it's smaller than what we're looking for, increase the minimum to move further along the array and test again!
    else:
        maximum -= 1 # If it's larger than what we're looking for, decrease the maximum to move backward along the array and test again!

# Make sure we actually found the number, rather than just running through the whole loop
if nums[mid] == searchFor:
    print "Found", searchFor, "at", mid
else:
    print "Could not find", searchFor
