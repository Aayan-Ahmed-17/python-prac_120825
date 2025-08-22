age = 18
x = 12
y = 23
z = 35

# PYTHON - Uses indentation (4 spaces recommended)
# if age >= 18:
#     print("You are an adult")
#     print("You can vote")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a child")

# Single line if (ternary-like)
status = "adult" if age >= 18 else "minor"
# print(status)

'''# Chained comparisons (PYTHON UNIQUE!)'''

# if y > x < z:                       #no need to type "and" keyword python speciality
#       print("running")

# if type(age) is int and len(status) >= 2:
#       print("All conditions true")

# else:
#       print(False)


'''# Membership testing'''
fruits = ["apple", "banana", "cherry", "melon", "lychee"]         #this is list == array of js

# if "mango" in fruits:
#       print("Yes!")
# else:
#       print("No")
      
# if "grape" not in fruits:
#       print("grape nahi hai")
# else:
#       print("grape hai")

'''# Identity testing'''

nothing = None

# if nothing is None:
#       print("Has no value")
# else:
#       print("has value")

'''Truthiness testing'''
empty_list = []
# if not empty_list:                        # More pythonic than len(empty_list) == 0
#     print("List is empty")

# name = ""
# if name:                                        # Checks if string is not empty
#     print(f"Hello, {name}")
# else:
#     print("Name is empty")


'''ex01 Basic Conditionals
Write a program that takes a number and prints whether it's positive, negative, or zero.
'''

# user_num = int(input("Enter num here : "))

# if user_num < 0: 
#       print(f"{user_num} is negative")
# elif user_num < 1: 
#       print(f"{user_num} is positive")
# else:
#       print(f"{user_num} is zero")

'''ex02 Grade Calculator
Create a function that converts numeric grades to letter grades:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
'''

user_score = int(input("Enter your score here : "))

if  90 <= user_score <= 100:
      print(f"{user_score} is b/w 90-100 (A)")
elif  80 <= user_score <= 89:
      print(f"{user_score} is b/w 80-89 (B)")
elif  70 <= user_score<= 79:
      print(f"{user_score} is b/w 70-79 (C)")
elif  60 <= user_score <= 69:
      print(f"{user_score} is b/w 60-69 (D)")
elif 0 <= user_score < 60:
      print(f"{user_score} is below 60 (F)")
else:
      print(f"{user_score} Please enter number 0 till 100")