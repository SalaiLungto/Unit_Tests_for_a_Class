# Program: student.py
# Author: Samuel Muang
# Course: Python (CIS189)
# Assignment: Student Class Unit Testing (Module 9 Topic 3)
# Last Date Modified: 10/24/2025
# This program run about defining a Student class with validation with a string representation method.

class Student:
    """Student class with validation for name, major, and GPA."""

    def __init__(self, lname, fname, major, gpa=0.0):
        # Validate last name: must contain only letters
        if not lname.isalpha():
            raise ValueError("Last name must contain only letters.")
        # Validate first name: must contain only letters
        if not fname.isalpha():
            raise ValueError("First name must contain only letters.")
        # Validate major: must contain only letters
        if not major.isalpha():
            raise ValueError("Major must contain only letters.")
        # Validate GPA: must be a float between 0.0 and 4.0
        if not isinstance(gpa, float) or not (0.0 <= gpa <= 4.0):
            raise ValueError("GPA must be a float between 0.0 and 4.0.")

        # Assign validated values to instance variables
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        """Returns a formatted string describing the student."""
        return f"{self.last_name}, {self.first_name} has major {self.major} with gpa: {self.gpa}"
