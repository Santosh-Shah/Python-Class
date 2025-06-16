# Python Scope
# 🔍 Scope = Where your variable lives
# There are 4 scopes:

# Local (inside a function)

# Enclosed (inside nested functions)

# Global (whole file)

# Built-in (Python keywords/functions)




# 💼 Used in:

# Avoiding variable name conflicts

# Secure and predictable code


x = "Global"

def callMe():
  x = "Local"
  print(x)



callMe()
print(x)
