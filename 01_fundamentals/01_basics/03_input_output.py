'''
input() takes inputs as a string
print() gives output as a string
'''


# type conversions of input() 
# user_age = int(input("Enter your age..."))
# height = float(input("Enter your height..."))

# a,b = input("enter something").split()                #two vals reqd not more or less to prevent errs   
# print(a,b, sep='|')


name = 'Alice'
age = 23
strike_rate = 130

# print(f"Name: {name}, Age: {age}, Score: {strike_rate : .1f}")          # .1f use to show only a single digit after decimal

# print with alignment and padding
text = "Python"
number = 42

# print(f"Left aligned: '{text:<10}'")
# print(f"Right aligned: '{text:>10}'")
# print(f"Center aligned: '{text:^10}'")
# print(f"Zero padded: '{number:05d}'")


'''ex 01 basic I/O
# Create a program that:
# 1. Asks for user's name, age, and city
# 2. Displays a formatted message using all three values
# 3. Use f-strings for formatting
'''

# input_name = input("Enter you name here")
# input_age = input("Enter you age here")
# input_city = input("Enter you city here")

# print(f"input_name: {input_name}, input_age: {input_age}, input_city: {input_city}")

'''ex02: Calculator Input
# Create a simple calculator that:
# 1. Asks for two numbers
# 2. Asks for operation (+, -, *, /)
# 3. Performs calculation and displays result
# 4. Handles invalid input gracefully
'''

a = int(input("Enter first number"))
b = int(input("Enter second number"))
opr = input("Enter operator (+, -, /, *)")
if opr == "+":
      result = a+b
if opr == "-":
      result = a-b
if opr == "/":
      result = a/b
if opr == "*":
      result = a*b

print(result)


'''ex04 Formatting Practice
# Given: name="John", age=25, salary=50000.75, gpa=3.67
# Print using different formatting methods:
# 1. "John (25) earns $50,000.75 with GPA: 3.7"
# 2. Right-align name in 10 characters
# 3. Display salary with comma separators
# 4. Show GPA with 1 decimal place
'''

name="John"
age=25
salary=50000.75
gpa=3.67

print(f"{name} ({age}) earns ${salary} with GPA: {gpa}")
print(f"{name: >10}")
print(f"{salary:}")
print(f"{gpa: .1f}")