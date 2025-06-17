# 🔹 Q1. Read & Display a File
# Create a text file called quotes.txt with 3 motivational quotes.
# Now write a program to open that file and print each line.

# creating files
# open("quotes.txt", "x")

# writing three motivational quotes
# with open("quotes.txt", "w") as file:
#   file.write("The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it.")
#   file.write("\nBelieve you can and you’re halfway there.")
#   file.write("\nDon’t watch the clock; do what it does. Keep going.")
  


# reading the file
# with open("quotes.txt", "r") as file:
#   content = file.read()
#   print(content)


with open("quotes.txt", "r") as file:
  for line in file:
    print(line.strip())




