# 🔹 Q9. Search a Word in a File
# Ask the user for a word
# Search if the word exists in mynote.txt, and print Found or Not Found.


userWord = input("Enter you word: ")

with open('mynote.txt', 'r') as file:
  content = file.read()
  if userWord in content:
    print("Found")
  else:
    print("Not Found")