# 🔹 Q3. Count Words in a File
# Write a program that:

# Reads from story.txt

# Counts the total number of words

# Hint: use .split() after reading the file content.


# open("story.txt", "x")


# with open("story.txt", "w") as file:
#   file.write("this story of santosh shah a software developer")


with open("story.txt", "r") as file:
  for textLine in file:
    print(textLine.split())

















