# Program: main.py
# Author: Samuel Muang
# Course: Python (CIS189)
# Assignment: Student Class Driver (Module 9 Topic 3)
# Last Date Modified: 10/24/2025
# This program runs for creating and printing Student objects.


from student import Student

def main():
    # This part is to create two valid Student objects
    student1 = Student("Duck", "Donald", "Physics", 3.6)
    student2 = Student("Mouse", "Minnie", "Art", 3.8)

    # This part is to print their string representations
    print(student1)
    print(student2)

if __name__ == "__main__":
    main()