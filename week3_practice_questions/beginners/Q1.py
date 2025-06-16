# Q1: Create a Class for Students
# Create a class Student with:

# Attributes: name, roll, marks

# Method: display() to print student info

# Then create 2 student objects and call the display method.


class Student:
  def __init__(self, name, roll, marks):
    self.name = name
    self.roll = roll
    self.marks = marks

  def display(self):
    print(f"Name: {self.name}")
    print(f"Roll No.: {self.roll}")
    print(f"Marks: {self.marks}")

  
std1 = Student("Santosh Shah", 45, 68.75)
std2 = Student("Hariom Shah", 22, 75.5)

std1.display()
print("-------------------")
std2.display()

