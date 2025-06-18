# 🔹 Q5. Create a Notes App (CLI)
# Ask user:

# Enter note title

# Enter note content

# Then:

# Save it as a text file like mynote.txt

# Format it like:

# Title: My Note
# ------------
# This is the content of my note.



title = input("Enter you title: ")
content = input("Enter you content: ")

# open("mynote.txt", "x")

with open("mynote.txt", "w") as file:
  file.write(f"Title: {title}\n---------------\n{content}")

# with open("week5_practice_questions/mynote.txt", "r") as file:
#   content = file.read()
#   print(content)

