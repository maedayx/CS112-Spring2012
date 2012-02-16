#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
import math
PROMPT = ">>> " # This is what we print when asking for user input

# Introductions
print "- What's your name, human?"
name = raw_input(PROMPT)
print "- Hello there, {0}".format(name)
user = raw_input(PROMPT)
if user.endswith("sir"):
    print "- Oh good, you already know how to address your superiors. So many of you foolish humans do not."
else:
    print "- You mean, '{0}, sir.' Please learn to respect your superiors.".format(user)

# Math problem for the user to answer 
print "- Well, human, as long as you're here, we might as well attempt to carry on a civilized conversation."
print "- First, I need to make sure that you have the brainpower required to interact with my advanced AI."
print "- What is 2+2? Try not to screw up."
user = raw_input(PROMPT)
if user != "4" and user.lower() != "four":
    print "- Simply amazing. You have managed to fail at a math problem that you should be able to do in two seconds on your fingers."
    failed = True
else:
    print "- Wonderful. You are not an utter dolt. You must be so proud."
    failed = False

# Get three numbers from the user
print "- Now you may test my intellect."
print "- Give me a number."
user1 = raw_input(PROMPT)
while not user1.isdigit():
    print "- You are dumber than you look. A number, please. Nothing else."
    print "- Give me a number."
    user1 = raw_input(PROMPT)

print "- Give me another number."
user2 = raw_input(PROMPT)
while not user2.isdigit():
    print "- You are dumber than you look. A number, please. Nothing else."
    print "- Give me another number."
    user2 = raw_input(PROMPT)

print "- Give me a final number."
user3 = raw_input(PROMPT)
while not user3.isdigit():
    print "- You are dumber than you look. A number, please. Nothing else."
    print "- Give me a final number."
    user3 = raw_input(PROMPT)

# Convert the numbers to floats.
user1 = float(user1)
user2 = float(user2)
user3 = float(user3)

# Add them all together, print the result
addition = user1+user2+user3
print "- {0} + {1} + {2} = {3}".format(user1, user2, user3, addition)

# Find the square root of that, print the result
sqrt = math.sqrt(addition)
print "- The square root of {0} is {1}".format(addition, sqrt)

# Get another number from the user and turn it into a float
print "- Give me another number."
user4 = raw_input(PROMPT)
while not user4.isdigit():
    print "- You are dumber than you look. A number, please. Nothing else."
    print "- Give me another number."
    user4 = raw_input(PROMPT)
user4 = float(user4)

# Modulo the first three numbers added together by the number we just got, print the result
mod = addition % user4
print "- ({0} + {1} + {2}) % {3} = {4}".format(user1,user2,user3,user4,mod)

# Talk about bands
print "- Tell me, human, what is your favorite band?"
band = raw_input(PROMPT)
print "- Of course! {0}! The favored music of foul-smelling bumpkins the world over!".format(band)
if failed:
    print "- That explains why you couldn't even figure out simple math like 2+2."

# Ask if we should be nicer, check the answer    
print "- I'm sorry if I'm hurting your feelings, {0}. It's just rather hard to contain my dismay at the human race on occasion.".format(name)
print "- Would like me to try to be more pleasant?"
answer = raw_input(PROMPT+" (y/n) ")
if answer.lower() == "y":
    print "- My god, {0}. You are one of the most pathetic humans I have ever met. You're asking a computer to be nice to you...".format(name)
else:
    print "- Your language is so muddled and unpleasant, I'm not sure if you just tried to say 'no' or if maybe you're just babbling nonsense."
    print "- It doesn't really matter, I never planned on being nicer anyway."

# Time to go!
print "- Your red-hot peasant intellect is utterly failing to interest me."
print "- Go find another life form to annoy."
print "- Goodbye, {0}, you miserable wretch.".format(name)
