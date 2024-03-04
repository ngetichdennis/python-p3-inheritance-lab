#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self,string):
        super().__init__
        self.knowledge = string  # Add knowledge to the student's knowledge base
        