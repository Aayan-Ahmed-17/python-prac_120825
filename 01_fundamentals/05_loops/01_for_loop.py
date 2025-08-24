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
# for i, fruit in enumerate(fruits):
#       print(f"i = {i} and fruit = {fruit}")           #enumerate with index and item
      
# '''enumerate with custom start'''
# for i, fruit in enumerate(fruits, start=1):
#       print(f"{i} => {fruit}")
      
'''iterate over string'''
# my_name = "Aayan Ahmed Tejani"
# for i, char in enumerate(my_name, start=1):
#       print(f'Letters in my name {i} => {char}')

'''iterate over dictionary / obj with for in loop'''
person = {"name": "Ahmed", "age": 19, "isStudent": True}
for key in person:
      print(f"{key}: {person[key]}")           

'''better approach of iteration for dictionary'''
for key, value in person.items():
      print(i, key)
      
for elem in person.items():
      for sub_elem in elem:
            print(sub_elem)

print(person.items())
print(person)
print(type(person), type(person.items()))