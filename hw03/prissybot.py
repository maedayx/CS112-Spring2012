#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

name = raw_input("- What's your name, human?\n>>> ")
print "- Hello there, %s" % name
user = raw_input(">>> ")
if user.endswith("sir"):
    print "- Oh good, you already know how to address your superiors. So many of you foolish humans do not."
else:
    print "- You mean, '%s, sir.' Please learn to respect your superiors." % user
    
print "- Well, human, as long as you're here, we might as well attempt to carry on a civilized conversation."
print "- First, I need to make sure that you have the brainpower required to interact with my advanced AI."
user = raw_input("- What is 2+2? Try not to screw up.\n>>> ")

user = user.lower()

if user != "4" and user != "four":
    print "- Simply amazing. You have managed to fail at a math problem that you should be able to do in two seconds on your fingers."
    failed = True
else:
    print "- Wonderful. You are not an utter dolt. You must be so proud."
    failed = False

print "- Now you may test my intellect."

user1 = raw_input("- Give me a number.\n>>> ")
while not user1.isdigit():
    print("- You are dumber than you look. A number, please. Nothing else.")
    user1 = raw_input("- Give me a number.\n>>> ")

user2 = raw_input("- Give me another number.\n>>> ")
while not user2.isdigit():
    print("- You are dumber than you look. A number, please. Nothing else.")
    user2 = raw_input("- Give me another number.\n>>> ")

user3 = raw_input("- Give me a final number.\n>>> ")
while not user3.isdigit():
    print("- You are dumber than you look. A number, please. Nothing else.")
    user3 = raw_input("- Give me a final number.\n>>> ")

user1 = float(user1)
user2 = float(user2)
user3 = float(user3)

addition = user1+user2+user3

print "- {0} + {1} + {2} = {3}".format(user1, user2, user3, addition)

sqrt = addition**.5

print "- The square root of {0} is {1}".format(addition, sqrt)

user4 = raw_input("- Give me another number.\n>>> ")
while not user4.isdigit():
    print("- You are dumber than you look. A number, please. Nothing else.")
    user4 = raw_input("- Give me another number.\n>>> ")
user4 = float(user4)

mod = addition % user4

print "- ({0} + {1} + {2}) % {3} = {4}".format(user1,user2,user3,user4,mod)

band=raw_input("- Tell me, human, what is your favorite band?\n>>> ")

print "- Of course! {0}! The favored music of foul-smelling bumpkins the world over!".format(band)
if failed == True:
    print "- That explains why you couldn't even figure out simple math like 2+2."
    
print "- I'm sorry if I'm hurting your feelings, {0}. It's just rather hard to contain my dismay at the human race on occasion.".format(name)
answer = raw_input("- Would like me to try to be more pleasant?\n>>> (y/n) ")
answer = answer.lower()
if answer == "y":
    print "- My god, {0}. You are one of the most pathetic humans I have ever met. You're asking a computer to be nice to you...".format(name)
else:
    print "- Your language is so muddled and unpleasant, I'm not sure if you just tried to say 'no' or if maybe you're just babbling nonsense."
    print "- It doesn't really matter, I never planned on being nicer anyway."

print "- Your red-hot peasant intellect is utterly failing to interest me.\n- Go find another life form to annoy."
print "- Goodbye, {0}, you miserable wretch.".format(name)
