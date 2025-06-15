# Question 9: (Match Case)
# Q: Use a match statement to check a variable called choice.
# If:

# 1 → print "Add"

# 2 → print "Edit"

# Anything else → print "Invalid"

choice = 3

match choice:
  case 1:
    print("Add")
  case 2:
    print("Edit")
  case _:
    print("Invalid")