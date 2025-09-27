'''Exercise 1: Basic Data Types
# Create variables of different types and print their types
# Create: an integer, float, string, boolean, and list
# Print each variable and its type using type() function
'''

string = "this is a string"
also_string = "77"
integer = 55
float_num = 7.89
is_available = True
values = [1, 2, True, False, "here", "three", "3"]

# print(string, also_string, integer, float_num, is_available, values, sep='\n')
# print(type(string), type(also_string), type(integer), type(float_num), type(is_available), type(values), sep='\n')

'''ex02 arithematic opr
# Given two numbers, perform all arithmetic operations
a = 15
b = 4
# Calculate and print: addition, subtraction, multiplication, 
# division, floor division, modulus, and exponentiation
'''
a = 15
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division= a // b
modulus = a % b
exponentiation = a ** b

# print(addition, subtraction, multiplication, division, floor_division, modulus, exponentiation, sep='\n')

'''ex03 Str operators
# Given a string, perform various operations
text = "Python Programming"
# Print: length, uppercase, lowercase, first 6 characters, last 11 characters
'''

text = "Python Programming"
# print(text, len(text), text.upper(), text.lower(), text[0 : 6], text[-11:], sep='\n')           #text[-11:] =. "Programming"; text[-11] =. P  giving letter on 11th index from last

'''ex 04 List operations
# Create a list of numbers and perform operations
numbers = [1, 2, 3, 4, 5]
# Add number 6, remove number 3, find length, check if 4 is in list
'''

numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.append(6)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# print(len(numbers))
# print(numbers.__contains__(4))

'''ex05 Boolean prac
# Given values, create boolean expressions
x = 10
y = 5
z = 15
# Create expressions using and, or, not operators that evaluate to True and False
'''
x = 10
y = 5
z = 15

# print(x > y and y < z)
# print(x < y or y > z)
# print(x >= z or y <= x)
# print(x <= z and True >= False)                 #True
# print(z < x and not x)

'''ex 06
How can you access a specific character within a string?
'''
target_character = "Hello World"
# print(target_character[0])

print(list("apple,banana,cherry"))	
print("-".join(['A', 'B', 'C']))	