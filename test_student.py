# Program: test_student.py
# Author: Samuel Muang
# Course: Python (CIS189)
# Assignment: Student Class Unit Testing (Module 9 Topic 3)
# Last Date Modified: 10/24/2025
# This program demonstrates about testing the Student class using the unittest framework of Python.


import unittest
from student import Student

class TestStudent(unittest.TestCase):
    """Unit tests for the Student class."""

    def setUp(self):
        # Create a sample student object before each test
        self.student = Student("Duck", "Daisy", "Music", 3.5)

    def tearDown(self):
        # Clean up after each test
        del self.student

    def test_object_created_required_attributes(self):
        # Test constructor with only required attributes
        s = Student("Duck", "Daisy", "Music")
        self.assertEqual(s.last_name, "Duck")
        self.assertEqual(s.first_name, "Daisy")
        self.assertEqual(s.major, "Music")
        self.assertEqual(s.gpa, 0.0)

    def test_object_created_all_attributes(self):
        # Test constructor with all attributes
        s = Student("Duck", "Daisy", "Music", 3.5)
        self.assertEqual(s.last_name, "Duck")
        self.assertEqual(s.first_name, "Daisy")
        self.assertEqual(s.major, "Music")
        self.assertEqual(s.gpa, 3.5)

    def test_student_str(self):
        # Test the string representation of the student
        expected = "Duck, Daisy has major Music with gpa: 3.5"
        self.assertEqual(str(self.student), expected)

    def test_object_not_created_error_last_name(self):
        # Test invalid last name (contains digits)
        with self.assertRaises(ValueError):
            Student("123", "Daisy", "Music")

    def test_object_not_created_error_first_name(self):
        # Test invalid first name (contains digits)
        with self.assertRaises(ValueError):
            Student("Duck", "123", "Music")

    def test_object_not_created_error_major(self):
        # Test invalid major (contains digits)
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "123")

    def test_object_not_created_error_gpa_non_float(self):
        # Test GPA with non-float value
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "Music", "A")

    def test_object_not_created_error_gpa_out_of_range(self):
        # Test GPA out of valid range
        with self.assertRaises(ValueError):
            Student("Duck", "Daisy", "Music", 5.0)

if __name__ == "__main__":
    unittest.main()