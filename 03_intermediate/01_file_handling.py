"""
ex01:Write a program that reads a text file and displays its contents on the screen.
Skills tested: open(), read(), context managers
"""

# Without using context managers
f = open("dummy.txt", "r")
content = f.read()

# Using context managers
with open("dummy.txt", "r") as f:
    content = f.read()
    # print(f.name, f.mode, f.closed, sep="\n")  # isClosed -> false

# print(f.closed)  # isClosed -> True

"""
ex02: Create a program that counts the number of lines in a text file.
Skills tested: readlines() or iteration, basic file operations
"""

#using readlines()
def count_files_with_readlines(filepath):
    """
    Counts the number of lines in a file using the readlines() method.
    """
    try:
      with open(filepath, 'r') as file:
         content = file.readlines()
    except:
      print('An exception occurred')