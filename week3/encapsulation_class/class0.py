#  Encapsulation
# 🔍 What is it?
# Hiding internal details from the outside world.
# We use private variables and getter/setter methods.


# 💼 Use:
# Used in banking systems, login systems, etc.

# Protects sensitive data


class Account:
  def __init__(self, balance):
    self.__balance = balance   #private

  def get_balance(self):
    return self.__balance
  
  def deposit(self, amount):
    self.__balance += amount


# Objects
account1 = Account(35000)
print("Initial Balance: ", account1.get_balance())

account1.deposit(15000)
print("Current Balance: ", account1.get_balance())
