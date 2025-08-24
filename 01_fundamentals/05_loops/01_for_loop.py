'''
Not uses for loop syntax as js do instead uses for-in loop of js kind of syntax
'''

fruits = ["apple", "banana", "pineapple"]                   #list / array of fruits
# for fruit in fruits:
#       print(fruit)
      
'''iterate over range'''
# for i in range(2, 10):                                #if one arg in range(n) then will go "0" to "n" if two args in range(n1, n2) then will go "n1" to "n2"
#       print(f"i => {i}")
      
# for i in range(0, 14, 3):                             #starting from 0 going to 14 and skipping two nums after each third number [0, 3, 6, 9 ... 12]
#       print(f"hello {i}")

'''range with enumerate for index and value'''
for i, fruit in enumerate(fruits):
      print(f"i = {i} and fruit = {fruit}")           #enumerate with index and item
      
'''enumerate with custom start'''
for i, fruit in enumerate(fruits, start=1):
      print(f"{i} => {fruit}")