# 🔹 Q4. Math Module – Geometry
# Write a function to:

# Take radius input from user

# Calculate and print area of a circle using math.pi
# area of a circle are: A = Pi*r^2

import math

radius = int(input("Enter number: "))

def areaOfCircle(radius):
  return math.pi * math.pow(radius, 2)

print("Area of Circle: ", areaOfCircle(radius))
print(math.pow(5, 2))
