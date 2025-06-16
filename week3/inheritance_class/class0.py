# what is inheritance?
# -> Inheritance let you reuse another class's properties(parent class) and methods

# example:
# a child inherits wealth from parent


# 💼 Use:
# Base class: User, Derived classes: Admin, Customer

# Common UI elements (Button → SubmitButton, CancelButton)




class Animal:
  def speak(self):
    print("It is from Animal Class")

class Cat():
  def mew(self):
    print("It is from Cat Class")

cat1 = Cat(Animal)
cat1.mew()
cat1.speak()