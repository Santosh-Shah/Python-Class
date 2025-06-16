# Q6: OOP Calculator
# Create a class Calculator with methods:

# add(a, b)

# subtract(a, b)

# multiply(a, b)

# divide(a, b)

# Create object and test all methods.



class Calculator:
  def add(self, a, b):
    print(f"Addition of {a} and {b}: {a + b}")
  
  def subtract(self, a, b):
    print(f"Subtraction of {a} and {b}: {a - b}")

  def multiply(self, a, b):
    print(f"Multiplication of {a} and {b}: {a * b}")

  def divide(self, a, b):
    print(f"Division of {a} and {b}: {a / b}")


cal1 = Calculator()
cal1.add(5, 4)
cal1.subtract(10, 11)
cal1.multiply(5, 9)
cal1.divide(81, 9)