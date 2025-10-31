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


# using readlines()
def count_lines_with_readlines(filepath):
    """
    Counts the number of lines in a file using the readlines() method.
    """
    try:
        with open(filepath, "r") as file:
            content = file.readlines()
            return len(content)
    except:
        raise (f"File {filepath} not found")


file_name = "dummy.txt"
total_lines = count_lines_with_readlines(file_name)

# print(f"File: {file_name}")
# print(f"Total number of lines (readlines() Method): **{total_lines}**")


# using readline()
def count_lines_readline(filepath):
    """
    Counts the number of lines in a file using readline mthd.
    """
    total_lines = 0
    try:
        with open(filepath, "r") as file:
            line = file.readline()
            while line:
                line = file.readline()
                total_lines += 1
            print(total_lines)
    except:
        print("An exception occurred")


# count_lines_readline("dummy.txt")


# using iteration method | recommended
def count_lines_efficiently(filepath):
    """
    Counts the number of lines in a file by iterating over the file object.
    """
    line_count = 0
    try:
        with open(filepath, "r") as file:
            for line in file:
                line_count += 1

            print(line_count)
    except:
        print("An exception occurred")


# count_lines_efficiently("dummy.txt")


