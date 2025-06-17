# 🔹 Q3. Date and Time
# Write a program to:

# Print the current date and time in format: YYYY-MM-DD HH:MM

# Print what day of the week it is (Monday, Tuesday...)



import datetime

now = datetime.datetime.now()
output = now.strftime("%Y-%m-%d %H:%M")
print("Date and Time: ", output)
print("Todays is: ", now.strftime("%A"))