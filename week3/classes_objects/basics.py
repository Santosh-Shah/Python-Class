# Python Classes and Objects
# 🔍 Class = Blueprint
# 🔍 Object = Real thing created from that blueprint


# 📌 Used in:

# Backend apps (users, posts, comments)

# Games (Player, Enemy, Level)

# GUI (Window, Button, Form)


class Person:
  def __init__(self, name, age):
    self.name1 = name
    self.age1 = age
    self.random1 = "Just for fun"
  
  def say_greet(self):
    print(f"Your name is: {self.name1}")
    print(f"Your age is: {self.age1}")
    print("Random Call: ", self.random1)


person1 = Person("Hariom Shah", 23)
person1.say_greet()

print("----------------------------")

person2 = Person("Santosh Shah", 25)
person2.say_greet()




# 🔹 __init__() is a constructor. Runs when you create object.
# 🔹 self refers to the current object.
