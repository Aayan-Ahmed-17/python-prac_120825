# Basic function definition
# def greet():
#       '''docstring comment, used to indicate purpose of a func'''
#       print("Hello, Dev")

# greet()     #function call

# def greet_name(name):
#       '''greets with capitalized name'''
#       print(f"Hello! Sir {name.capitalize()}")
      

# greet_name("aayan ahmed")

# def add_two_numbers(a, b):
#       '''returns sum of two numbers'''
#       return  a + b

# print(add_two_numbers(11, 5))

# def mul_two_numbers(a, b = 1):
#       return a*b

# print(mul_two_numbers(5))

'''ex01
Create a function called calculate_area that takes length and width as arguments. The width argument should have a default value of 10. The function should return the calculated area.'''

# def calculate_area(len, width = 10):
#       return len * width

# print(calculate_area(4, 2))
'''ex02
Write a function called get_user_info that takes a first_name and last_name as arguments and returns a tuple containing the full name and the length of the full name. For example, for "John" and "Doe", it should return ("John Doe", 8).'''

def get_user_info(f_name, last_name):
      full_name = f"{f_name} {last_name}"
      return (full_name, len(full_name))

print(get_user_info("Aayan", "Ahmed"))