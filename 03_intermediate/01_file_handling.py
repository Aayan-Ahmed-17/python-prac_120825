'''
ex01:Write a program that reads a text file and displays its contents on the screen.
Skills tested: open(), read(), context managers
'''

# Without using context managers
f = open('dummy.txt', 'r')
content = f.read()

#Using context managers
with open('dummy.txt', "r") as f:
    content = f.read()
    print(f.name, f.mode, f.closed sep='\n')            #isClosed -> false

print(f.closed)             #isClosed -> True


