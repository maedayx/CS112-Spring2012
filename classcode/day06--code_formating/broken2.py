#!/usr/bin/env python
from random import randint

s = 1
randomNumbers = []
PROMPT = ">>> "

# Get a number from the user and create a list of that many random numbers.
theRange = int(raw_input(PROMPT))
for x in range(theRange):
    randomNumbers.append(randint(0,20))

# Output the numbers.
print "Here are the random numbers I generated: "
print randomNumbers

# Sort the list of random numbers from
while s:
    s = 0
    for i in range(1,theRange):
        if randomNumbers[i-1] > randomNumbers[i]:
            temp1 = randomNumbers[i-1]
            temp2 = randomNumbers[i]
            randomNumbers[i-1] = temp2
            randomNumbers[i] = temp1
            s = 1

print "And here they are sorted from smallest to largest: "
print randomNumbers