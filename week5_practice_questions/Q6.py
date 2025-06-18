# 🔹 Q6. Use String Formatting
# Take name and score from user
# Print:
# Hello Santosh, you scored 95% in Python. using all 3 formatting methods (%, .format(), f-string)



name = input("Enter your name: ") 
score = input("Enter you score: ")         

print("Hello! %s, you scored %s%% in python. " % (name, score))
print("Hello! {}, you scored {}% in python. ".format(name, score))
print(f"Hello! {name}, you scored {score}% in python")