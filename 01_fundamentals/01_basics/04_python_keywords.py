'''
Python has reserved keywords, they can't be used as a variable name.
'''
import keyword

print("keyword")
print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(f"The total numbers of reserved keywords are: {len(keyword.kwlist)}")

print(keyword.iskeyword("if"))                  #isKeyword() gives True / False