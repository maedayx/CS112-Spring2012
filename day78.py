#! /usr/bin/env python

file_out = open("thisIsText.txt", "w")
file_out.write("HAHA TEXT")
file_out.close()

try:
    file_in = open("thisIsText.txtOP_THIS_IS_SPELLED_WRONG", "r")
    for line in file_in:
        print line
    file_in.close()
    print 1/0
except IOError:
    print "Shit broke!"
except ZeroDivisionError:
    print "What, do you want a black hole?"

print "But we're still alive."