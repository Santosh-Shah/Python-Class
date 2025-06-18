# 🔹 1. Python File Handling
# Used to read from or write to files like .txt, .json, .csv, etc.



# ✍️ Create to a File
# open("info.txt", "x")



# ✍️ Read from a File
# with open("info.txt", "r") as file:
#   content = file.read()
#   print(content)




# ✍️ Write to a File
# with open("info.txt", "w") as file:
#   file.write("Hello! Santosh how are you?")



# ✍️ Append to a File
# with open("info.txt", "a") as file:
#   file.write("\nHello! Hariom how are you?")


# ✍️ Delete to a File

import os

if os.path.exists("info.txt"):
  os.remove("info.txt")
else:
  print("File doesn't exit")


