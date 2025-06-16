# Polymorphism
# 🔍 What is it?
# Same method name, different behavior depending on object type.


# 💼 Use:

# Common interface (e.g., .render(), .draw()) across different elements

# REST API returning different types of users



class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

# Polymorphism
for animal in [Cat(), Dog()]:
    animal.speak()

# animal1 = Cat()
# animal1.speak()

# animal2 = Dog()
# animal2.speak()









