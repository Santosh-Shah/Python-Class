# Question 5: (Boolean + Comparison)
# Q: Write a program that checks if a user is an adult (age 18+). Store the age in a variable and use an if condition to print "Adult" or "Minor".

age = int(input("Enter you age: "))
if age >= 18:
  print("Adult")
else: 
  print("Minor")