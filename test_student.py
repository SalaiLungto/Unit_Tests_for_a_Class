# Program: test_student.py
# Author: Samuel Muang
# Course: Python (CIS189)
# Assignment: Student Class Unit Testing (Module 9 Topic 3)
# Last Date Modified: 10/24/2025
# This program demonstrates about testing the Student class using the unittest framework of Python.


import unittest
from student import Student

class TestStudent(unittest.TestCase):
    """The unit tests for the Student class."""

    def setUp(self):
        # This is to create a sample student object before each test
        self.student = Student("Duck", "Daisy", "Music", 3.5)

    def tearDown(self):
        # This part is to clean up after each test
        del self.student

    def test_object_created_required_attributes(self):
        # This part tests constructor with only required attributes
        s = Student("Duck", "Daisy", "Music")
        self.assertEqual(s.last_name, "Duck")
        self.assertEqual(s.first_name, "Daisy")
        self.assertEqual(s.major, "Music")
        self.assertEqual(s.gpa, 0.0)

    def test_object_created_all_attributes(self):
        # This part tests constructor with all attributes
        s = Student("Duck", "Daisy", "Music", 3.5)
        self.assertEqual(s.last_name, "Duck")
        self.assertEqual(s.first_name, "Daisy")
        self.assertEqual(s.major, "Music")
        self.assertEqual(s.gpa, 3.5)

    def test_student_str(self):
        # This part is to test for the student's string representation
        expected = "Duck, Daisy has major Music with gpa: 3.5"
        self.assertEqual(str(self.student), expected)

    def test_object_not_created_error_last_name(self):
        # This test is with invalid last name (for contains digits)
        with self.assertRaises(ValueError):
            Student("123", "Daisy", "Music")

    def test_object_not_created_error_first_name(self):
        # This test is with invalid first name (for contains digits)
        with self.assertRaises(ValueError):
            Student("Duck", "123", "Music")

    def test_object_not_created_error_major(self):
        # This test is also with invalid major (for contains digits)
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "123")

    def test_object_not_created_error_gpa_non_float(self):
        # This part tests GPA with non-float value
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "Music", "A")

    def test_object_not_created_error_gpa_out_of_range(self):
        # This test GPA out of valid range
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "Music", 5.0)

if __name__ == "__main__":
    unittest.main()