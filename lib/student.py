#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Initialize parent class (User)
        self.knowledge = []  # Initialize the knowledge attribute as an empty list

    def learn(self, fact):
        self.knowledge.append(fact)  # Add a new fact to the knowledge list

 