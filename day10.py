#! /usr/bin/env python

matrix = ["hello", 2.0, 5, [10, 20]]
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'

people = {  'jonah' : 'stupid',
            'jack' : 'ugly',
            'alec' : 'smelly',
            'paul' : 'awesome'}

name = raw_input("Your name: ")

if name.lower() in people:
    print name, "is", people[name.lower()]
else:
    print "I don't know you,", name

for k,v in eng2sp.items():
    print k,v
    
s = 'Monty Python'
print s[6:12] # Get a slice of a string