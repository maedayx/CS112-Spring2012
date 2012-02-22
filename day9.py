#! /usr/bin/env python

import math

def fToC (temp):
    cent = temp-32
    cent *= 5
    cent /= 9
    return cent
    
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
    
#num = int(raw_input("Enter a temperature in F: "))
#print "In C, that is", fToC(num)

out1, out2 = quadratic(1,6,3)
print out1
print out2