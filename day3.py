#! /usr/bin/env python
n = 17
pi = 3.141592
otherfloat = 4.2
message = "Trololol\n"
message0 = "The Trollface says: "
final = message0+message # Concatenation!
otherfloat+=1 # We can't do ++ in python. LAME.

message = bool(message)

print type(message)
print message
print pi // otherfloat #force python to do integer division
print pi ** otherfloat # ** -> "to the power of"
print n % otherfloat # Modulo duh
print final
print final * 8
print otherfloat

print "You there! What's your name, boy?"
name = raw_input()
print "Oh...hi, %s" % (name)

piglatin = raw_input()
print "%s-%say" % (piglatin[1:], piglatin[0])

