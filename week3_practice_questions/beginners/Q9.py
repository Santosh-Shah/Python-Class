# 🔹 Q9: Iterators in OOP
# Create a class MyNumbers that creates an iterator from 1 to 3.

# Use next() and for loop to print numbers.

class MyNumbers:
    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        if self.current <= 3:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Create iterator object
nums = MyNumbers()
it = iter(nums)

# Using next()
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# Using for loop
for n in MyNumbers():
    print(n)