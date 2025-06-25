# ✅ 2. Nested Functions (Closures)

# def outer():
#     def inner():
#         print("I am the inner function.")


#     print("from Outer function")
#     inner()

# outer()


# def outer(x):
#   def inner(y):
#     return x + y
  
#   return inner

# innerR= outer(5)
# outerR = innerR(4)
# print(f"Output: {outerR}")




def greet(name):
  def msg():
    return "Hi! " + name
  return msg

output = greet("Hariom Shah")
print(output())



