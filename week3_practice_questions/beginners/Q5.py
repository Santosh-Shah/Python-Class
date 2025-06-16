# 🔹 Q5: Polymorphism Example
# Create two classes:

# Cat → method sound() → prints "Meow"

# Dog → method sound() → prints "Bark"

# Write a function make_sound(animal) that takes an object and calls .sound() on it.


class Cat:
  def sound(self):
    print("Meow")

class Dog:
  def sound(self):
    print("Bark")

def make_sound(animal):
  animal.sound()


cat = Cat()
dog = Dog()

make_sound(cat)
make_sound(dog)
