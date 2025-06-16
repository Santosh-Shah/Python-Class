# 6. re — Regular Expressions
# 👇 Why?
# To validate patterns like:

# Email 📧

# Phone 📱

# Password strength 🔐


# 💼 Used in:
# Form validation

# Log file scanning

# Crawlers, scrapers

import re

email = "shasantosh679@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
  print("Valid email")
else:
  print("Invalid email")