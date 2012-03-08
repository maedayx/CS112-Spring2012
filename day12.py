#! /usr/bin/env python

class Student(object):
    def __init__(self, name="Jane Doe"):
        self.name = name
    def say(self, message):
        print self.name+": "+message
    def say_to(self, other, message):
        self.say(message+", "+other.name)
    def print_me(self):
        print self.name
        
class Course(object):
    def __init__(self, name):
        self.name = name
        self.enrolled = []
    def enroll(self, student):
        self.enrolled.append(student)
    def print_me(self):
        for student in self.enrolled:
            student.print_me()
    
bob = Student("Bob")
fred = Student()

cs112 = Course("CS112")
cs112.enroll(bob)
cs112.enroll(fred)
cs112.print_me()
