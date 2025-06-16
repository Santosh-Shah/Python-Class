# 🔹 2. Modules — Reusable Code
# 👇 Why?
# To avoid writing the same code again and again.

# 💼 Real Usage:
# Organizing large backend apps

# Shared code in teams

# APIs, auth, utils, config files


import math
import myMath
import datetime

print(math.sqrt(9))
print(math.factorial(4))
print(math.pi)
print(math.fabs(5))
print(myMath.addMath(45, 6))


now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))