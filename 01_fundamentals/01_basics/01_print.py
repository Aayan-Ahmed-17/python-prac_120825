# hello world | different types of print
#print("hello world")
#print("first", "second", "third", sep=' | ')  #by-default sep is single space, we can change like this
#print("Now", "I", "gonna", "try", "end", "arg", sep="~", end="...")  #places content at the end of the whole sentence

#============Rules===============
"""
1-Parentheses are required in Python 3: print("text") not print "text"
2-Case sensitive: print() works, Print() doesn't
3-Strings must be quoted: Single ' or double " quotes
4-Indentation matters (we'll see this later)
"""


#===========Types of Errors=============
"""
# ERROR: Missing quotes
print(Hello World)  # NameError: name 'Hello' is not defined

# ERROR: Missing parentheses  
print "Hello"  # SyntaxError (Python 3)

# ERROR: Mismatched quotes
print("Hello')  # SyntaxError: unterminated string literal

# ERROR: Case sensitivity
Print("Hello")  # NameError: name 'Print' is not defined
"""


#=============Exercises===========================
""" ex01
# Write a program that prints:
# Line 1: Your name
# Line 2: Your favorite programming language
# Line 3: A motivational quote
# Make sure each is on a separate line      
"""

# print("Aayan Ahmed")
# print("Javascript")
# print("A dog can only barks at lion for himself \n but the same dog can fight with lion to protect his owner")

"""ex 02
# Create a program that prints this exact output:
# Name: John | Age: 25 | City: New York
# Use variables and the sep parameter
"""

# print("Name: John", "Age: 25", "City: New york", sep=' | ')


r'''ex 03
Print this exact text:
The file path is: C:\Users\Python\Documents
She said, "Python is awesome!"
Column1     Column2     Column3
'''

print("The file path is: C:\\Users\\Python\\Documents")
print('She said, "Python is awesome!"')
print("Column1\t\tColumn2\t\tColumn3")