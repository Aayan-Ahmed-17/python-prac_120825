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
print(mobile1.model_name, mobile1.brand ,sep='\n')

mobile1.price = 600000
print(mobile1.model_name, mobile1.brand, mobile1.price ,sep='\n')


