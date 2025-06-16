# Q3: Encapsulation
# Create a class BankAccount with:

# Private variable __balance

# Method deposit(amount) and get_balance()

# Try to print the balance directly (should give error), and then using method

class BankAccount:
  def __init__(self, balance):
    self.__balance = balance

  def get_balance(self):
    return self.__balance
  
  def deposit(self, amount):
    self.__balance += amount


# Creating objects
bank1 = BankAccount(10000)
print("Initial Balance: ", bank1.get_balance())
bank1.deposit(15000)
print("Current Balance: ", bank1.get_balance())

print("--------------------------------------------------")

bank2 = BankAccount(25000)
print("Initial Balance: ", bank2.get_balance())
bank2.deposit(30000)
print("Current Balance: ", bank2.get_balance())
