'''Going to start py oop concept from very basics'''

'''Create class'''
class Car:
      standand = "Elite Class"      #class attribute

simple_obj = Car()
# print(simple_obj)

'''Class with class attr, init(), instance attr'''
class Mobile:
      brand = "Samsung"      #class attr | it's not imp | shared by all instances created by this class
      
      def __init__(self, model_name, price, is_new, in_stock):
            self.model_name = model_name
            self.price = price
            self.is_new = is_new
            self.in_stock = in_stock
            
mobile1 = Mobile("S 25 ultra", 500000, True, True)
# print(mobile1)
# print(Mobile)

'''Access props N manipulate them also'''
# print(mobile1.model_name, mobile1.brand ,sep='\n')

mobile1.price = 600000
# print(mobile1.model_name, mobile1.brand, mobile1.price ,sep='\n')

'''============================Exercises questions=========================='''

'''Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
'''

#my code
class Greeter:
      def __init__(self, name):
            self.name = name
            
      def greet(self):
            return f"Hello {self.name}"

user1 = Greeter("Aayan Ahmed")
print(user1.greet())

#greeek for greek code
class Greeter:
    def greet(self, name):
        print(f"Hello, {name}!")

# Example usage:
g = Greeter()
g.greet("Gabriel")


