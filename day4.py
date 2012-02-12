#! /usr/bin/env python

names = ['bob', 'fred astaire', 'swagnor mcduck']

letters = ['a','d','f']
letters[1:1] = ['b','c']

print letters[-1]

# letters2 references letters
letters2 = letters
letters[0] = 'huh'
print letters2

# letters3 is a copy of letters, and thus won't change when we change letters
letters3 = letters[:]
letters[0] = 'hah'
print letters3

titles = ['Hitchhikers Guide to the Galaxy', 'Restaurant at the End of the Universe', 'Life, the Universe and Everything']
print titles
titles.append("So Long and Thanks for all the Fish")
titles.append("Mostly Harmless")
print titles

for title in titles:
    print title
    
TAs = ["Alec","Jonah","Jack"]
nameIn = ""
#nameIn = raw_input("Enter a name: ")

if nameIn in TAs:
    print "Take a shower."
    
for i in range(1,11,2):
    print i