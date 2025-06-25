def greet(name):
  print(f"Hello ! {name}")

hello = greet
hello("Hariom Shah")


# Examples1

def addition(a, b):
  return a + b


def calculator(func, a, b):
  return func(a, b)

output = calculator(addition, 4, 10)
print(f"Output: {output}")


# ✅ 1.3 Return a Function from Another Function

def speak(text):
  def upperCase():
    return text.upper()
  
  return upperCase

call_speak = speak("Vedas College!")
print(call_speak())



# ✅ 1.4 Store Functions in Data Structures
def square(x): return x ** 2
def cube(x): return x ** 3

calculate = [square, cube]
for f in calculate:
  print(f"Output: {f(5)}")


