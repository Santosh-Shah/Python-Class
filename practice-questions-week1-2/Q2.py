# Q: Write a program that takes a number from the user and checks:
# If it is even, print "Even number".
# Else, print "Odd number".

# num1 = 501


# by taking number from user
num1 = int(input("Enter a number: "))
ans = num1 % 2
if ans == 0:
  print("Even number")
else:
  print("Odd number")


