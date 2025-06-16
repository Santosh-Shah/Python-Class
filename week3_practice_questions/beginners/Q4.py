# 🔹 Q4: Inheritance Example
# Create:

# Class Employee with method work()

# Class Manager that inherits Employee, adds method manage()

# Create object of Manager and call both methods.



class Employee:
  def work(self):
    print("Calling from Employee class")
  


class Manager(Employee):
  def manage(self):
    print("Calling from Manager class")


mngr1 = Manager()
mngr1.manage()
mngr1.work()


print("-------------------------")
mngr2 = Manager()
mngr2.work()
mngr2.manage()