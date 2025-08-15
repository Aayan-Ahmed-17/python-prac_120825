'''
Python has reserved keywords, they can't be used as a variable name.
'''
import keyword

# print("keyword")
# print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# print(f"The total numbers of reserved keywords are: {len(keyword.kwlist)}")

# print(keyword.iskeyword("if"))                  #isKeyword() gives True / False

'''ex01
# Identify which of these are Python keywords:
# print, if, hello, def, variable, class, True, 
# function, return, import, my_var, False, for
'''

# print(keyword.iskeyword("print"))                          #F
# print(keyword.iskeyword("if"))                                #T  
# print(keyword.iskeyword("hello"))                          #F
# print(keyword.iskeyword("def"))                             #T
# print(keyword.iskeyword("variable"))                      #F
# print(keyword.iskeyword("class"))                           #T
# print(keyword.iskeyword("True"))                            #T
# print(keyword.iskeyword("function"))                      #F
# print(keyword.iskeyword("return"))                          #T
# print(keyword.iskeyword("import"))                         #T
# print(keyword.iskeyword("my_var"))                         #F
# print(keyword.iskeyword("False"))                             #T
# print(keyword.iskeyword("for"))                                #T

'''ex 02
# Write a program using these keywords:
# if, else, for, in, def, return, try, except
# Create a function that processes a list of numbers and handles errors
'''

'''ex 03
# Use these built-in functions in a program:
# len(), max(), min(), sum(), type(), isinstance()
# Create a program that analyzes a list of mixed data types
'''

'''ex 04
# These variable names are invalid because they use keywords.
# Suggest better alternatives:
# class = "Python"
# if = True  
# for = [1, 2, 3]
# def = "function"
'''
lang = 'Python'
isValid = True
nums = [1, 2, 3]
purpose = "funciton"
