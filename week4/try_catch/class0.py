
# 1. try-except — Error Handling
# 👇 Why?
# To gracefully handle errors and avoid app crashes.


# 💼 Real Usage:
# Validating user input

# Handling file/database errors

# Preventing web app crashes




try:
  num = int(input("Enter a number: "))
  print(10 / num)
except ZeroDivisionError:
  print("You can't divide num by 0")
except ValueError:
  print("Invalid input")