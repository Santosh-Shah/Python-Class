# 🔹 Q4. Delete a File Safely
# Write a program that:

# Asks for a filename to delete

# Deletes it using os.remove() only if the file exists

import os

if os.path.exists("story.txt"):
  os.remove("story.txt")
else:
  print("File doesn't exit")