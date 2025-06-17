# 🔹 Q2. Write & Append to a File
# Ask the user to enter their name and favorite programming language.
# Then:

# Write this info to a file called devs.txt

# Each new user’s input should be added to the file (append mode)

name = input("Enter your name: ")
fav_lang = input("Enter your favorite programming language: ")

# open("devs.txt", "x")

# with open("devs.txt", "w") as file:
#   file.write(f"User name: {name} and Favorite Programming Language: {fav_lang}")

with open("devs.txt", "a") as file:
    file.write(f"\nUser name: {name} and Favorite Programming Language: {fav_lang}")