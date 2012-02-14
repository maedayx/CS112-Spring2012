#!/usr/bin/env python

# Declare our variables.
allNums = []
numIn = None
PROMPT = ">>> "

# Get a list of numbers from user and append them to allNums as floats.
while numIn != "":
    print "Please enter a number or press [Return] to continue!"
    numIn = raw_input(PROMPT)
    if numIn.isdigit():
        allNums.append(float(numIn))

# Find the total of the list of numbers.
total = 0
for num in allNums:
    total += num

# Output average of list.
print "The average of all of those is: "
print total/len(allNums)
