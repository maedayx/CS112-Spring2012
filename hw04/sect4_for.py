#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total = 0
for x in nums:
    total += x

print "1.", total


# 2. Print every even number in nums
print "2. even numbers"
only_even = True

for x in nums:
    if (x%2==0):
        print "\t", x
    else:
        only_even = False

# 3. Does nums only contain even numbers? 


print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
newNums = []
for x in range(0,100):
    if (x%2!=0):
        newNums.append(x)

print "4.", newNums

# 5. [ADVANCED]  Multiply each element in nums by its index


# print "5.", __
