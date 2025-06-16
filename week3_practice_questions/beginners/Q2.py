#  Q2: Add Constructor
# Modify the Student class to include a constructor (__init__) that sets the values when the object is created.

# # Example:
# s1 = Student("Santosh", 101, 85)



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