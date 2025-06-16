# 🔹 Q8: Class with Default Values
# Create a class User that accepts name, and sets status as "active" by default.

# Print both values.


class User:
  def __init__(self, name):
    self.name = name
    self.status = "active"

  def profile(self):
    print(f"User Name: {self.name}, Status: {self.status}")


user1 = User("Santosh Shah")
user2 = User("Hariom Shah")


user1.profile()
user2.profile()