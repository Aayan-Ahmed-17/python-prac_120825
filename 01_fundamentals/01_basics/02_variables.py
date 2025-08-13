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