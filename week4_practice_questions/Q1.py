# 🔹 Q1. Error Handling – Division
# Write a program that:

# Asks the user to enter two numbers

# Divides them

# Uses try-except to handle:

# Division by 0

# Non-numeric input


try:
  num1 = int(input("Enter number1: "))
  num2 = int(input("Enter number2: "))

  print(num1 / num2)
except ZeroDivisionError:
  print("Zero is not allowed!")
except ValueError:
  print("Invalid Input number")