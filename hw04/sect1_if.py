#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if (n%2==0):
    odd = False
    print "1. Even"
else:
    odd = True
    print "1. Odd"


# 2. If n is odd, double it
if odd:
    print "2.", n*2
else:
    print "2. Not Odd"


# 3. If n is evenly divisible by 3, add four
if (n%3==0):
    print "3.", n+4
else:
    print "3. Not divisble by 3"


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

letters = ["D","C","B","A"]

grade = grade/10

if (grade >= 6):
    print "4.",letters[grade-6]
else:
    print "4. F"

