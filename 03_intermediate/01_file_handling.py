'''
ex01:Write a program that reads a text file and displays its contents on the screen.
Skills tested: open(), read(), context managers
'''

# Without using context managers
f = open('dummy.txt', 'r')
content = f.read()
print(content)

#Using context managers
with open('dummy.txt', "r") as file:
    content = file.read()
    print(content)