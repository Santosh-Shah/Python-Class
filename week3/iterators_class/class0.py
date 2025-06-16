
#  Python Iterators
# 🔍 What is an Iterator?
# It allows looping over objects like lists, one element at a time.

# 💼 Used in:

# Reading large files

# Working with streams or live data




nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
