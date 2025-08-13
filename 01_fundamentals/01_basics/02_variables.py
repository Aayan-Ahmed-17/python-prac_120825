'''
01_numbers.py             # int, float, complex
02_strings.py             # String creation, methods, formatting
03_booleans.py            # True, False, logical operations
04_type_conversion.py     # Casting between types
05_constants.py           # Naming conventions for constants
data_types_exercises.py   # Practice problems
data_types_cheatsheet.md  # Quick reference
'''

'''=============Assigning nums variable ============'''
age = 19    #int number [num without decimal regardless of +/-]
height = 6.1      #float num  [num with decimal regardless of +/-]
equation = 12 + 7j      #complex num [this eqn type num, can only use "j", regardless of +/-]
height = "6.2"      #updating height 'cause vars are dynamic in .py

# print(age, height, equation, sep='\n')

'''================Multiple Assignment============'''
x,y,z = 1,2,3           #can asgn mul vals like arr destructing in js
# print(x,y,z)

'''===========Naming conventions in .py=================='''
camelCase = "avoid it for general use"
snake_case = "recommended for general use"
ALL_CAPS = "recommended for constants vals"
_single_leading_underscore = "recommended to use _ in the beginning for private variables"

# print(camelCase, snake_case, ALL_CAPS, _single_leading_underscore, sep='\n')


'''==================checkin' type n id of vars================'''
# print(type(snake_case), type(height), type(age), type(equation))
# print(complex)
# print(id(snake_case), id(height), id(age), id(equation))

'''===============Rules For Var Names===================='''
'''Must start with letter (a-z, A-Z) or underscore (_)
Can contain letters, digits (0-9), and underscores
Case sensitive: age and Age are different variables
Cannot use Python keywords: if, for, while, def, etc.'''

'''==============INVALID names===========
2user = "John"                # Cannot start with number
user-name = "John"       # Hyphens not allowed
user name = "John"       # Spaces not allowed
if = "John"                      # 'if' is a keyword
class = "Python"             # 'class' is a keyword'''


#List of reserved keywords in python
# import keyword;
# print(keyword.kwlist)

'''============Comon Errors============='''
# 2user = "John"                # invalid decimal literal
# user-name = "John"       # SyntaxError: cannot assign to expression here.
# user-name == "John"       # when print will give "NameError: name 'user' is not defined.""
# user name = "John"       # SyntaxError: invalid syntax
# if = "John"                      #SyntaxError: invalid syntax
# class = "Python"             #SyntaxError: invalid syntax

'''===============Exercises===================='''

'''ex01 "var creation"

# Create variables for:
# - Your first name
# - Your last name  
# - Your birth year
# - Your favorite number (decimal)
# - Whether you like programming (True/False)
# Print each variable with a descriptive label
'''

first_name, last_name, birth_year, favorite_decimal_number, is_like_programming = "Aayan", "Ahmed", 2006, 5.10, True

# print(f"first_name = {first_name}", f"last_name = {last_name}", f"birth_year = {birth_year}",f"favorite_decimal_number = {favorite_decimal_number}", f"is_like_programming = {is_like_programming}", sep='\n')

''' ex02 fix 'em\
# 1st_place = "Gold"
# user-email = "test@email.com"  
# class = "Python Programming"
# for = 100
# my var = "test"
'''

place1 = "Gold"                                       #can't start with num
user_email = "test@email.com"              #hyphen not allow
class_ = "Python Programming"             #keyword can't be declared as a variable name
for_ = 100                                               #keyword can't be declared as a variable name
my_var = "test"                                       #can't contain spaces

'''ex03 Variable Swapping
# Create two variables: a = 10, b = 20
# Swap their values without using a temporary variable
# Print the values before and after swapping
'''

a = 10
b = 20
# print(a, b)
a, b = b, a
# print(a, b)