# hello world | different types of print
print("hello world")
print("first", "second", "third", sep=' | ')  #by-default sep is comma, we can change like this
print("Now", "I", "gonna", "try", "end", "arg", sep="~", end="...")  #places content at the end of the whole sentence


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