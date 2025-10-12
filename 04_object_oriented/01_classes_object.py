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
'''# class Greeter:'''
#       def __init__(self, name):
#             self.name = name
            
#       def greet(self):
#             return f"Hello {self.name}"

# user1 = Greeter("Aayan Ahmed")
# print(user1.greet())

''' #greeek for greek code'''
# class Greeter:
#     def greet(self, name):
#         print(f"Hello, {name}!")

# # Example usage:
# g = Greeter()
# g.greet("Gabriel")

'''Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.'''
class Calculator: 
      def add(self, num1, num2):
            return num1 + num2
      def subtract(self, num1, num2):
            return num1 -  num2

calculation = Calculator()
# print(calculation.add(23, 6))
# print(calculation.subtract(2,16))

'''Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
Start: a = 1
Common difference: d = 2
n terms: 5
'''
class Employee:
      def __init__(self, name: str, id: int, salary: int):
            self.name = name
            self.id = id
            self.salary = salary

employee_1 = Employee("Owais", 123, 80000)
# print(employee_1.__dict__) # __dict__ used to view them like a dict or obj of js

'''exercise 04: Design a class SeriesCalculator that calculates the sum of an arithmetic series.'''
class SeriesCalculator:
    def calculate_sum(self, n, a=1, d=2):
        # Sum of the first n terms of an arithmetic series
        return n * (2 * a + (n - 1) * d) // 2

# Test the calculator
sc = SeriesCalculator()
# print("Sum of series:", sc.calculate_sum(6))

'''Exercise 5: Create a class MaxFinder that identifies the largest number in a list.'''

#my_solution
# class MaxFInder:
#       def __init__(self, num_list):
#             self.num_list = num_list
            
#       def find_max(self):
#             frst_elem = self.num_list[0]
#             for num in self.num_list:
#                   if num > frst_elem:
#                         frst_elem = num
#                   else:
#                         continue
            
#             return frst_elem

# lst_1 = MaxFInder([1,2,5,8,3,7,12,34,7])
# print(lst_1.find_max())

#web solution 
class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        if not self.numbers:
            return "List is empty"
        return max(self.numbers)

# Example
finder = MaxFinder([1,2,5,8,3,7,12,34,7])
# print("The largest number is:", finder.find_max())

'''Exercise 06: Create a BankAccount class
# - Instance variables: account_number, balance, owner_name
# - Methods: deposit(amount), withdraw(amount), get_balance()
# - Ensure balance never goes negative
'''

class BankAccount:
      def __init__(self, account_number, balance, owner_name):
            self.account_number = account_number
            self.balance = balance
            self.owner_name = owner_name
            
      def deposit(self, amount):
            self.balance += amount
      
      def withdraw(self, amount):
            if (amount <= self.balance): 
                  self.balance -= amount
            else:
                  print(f"Withdrawal failed for {self.owner_name}: Insufficient funds. Available: {self.balance}")
      
      def get_balance(self):
            return f"{self.owner_name} has {self.balance} amount in his account {self.account_number}"

owner_1 = BankAccount("ACC32134", 5000000, "Usman")
owner_2 = BankAccount("ACC45632", 20000, "Rafay")
# print(owner_1.__dict__, owner_2.__dict__, sep='\n')

owner_1.withdraw(4900000)
owner_2.deposit(480000)
# print(owner_1.__dict__, owner_2.__dict__, sep='\n')

'''Exercise 07: Create a TodoList class
# - Instance variable: tasks (list)
# - Methods: add_task(task), remove_task(index), show_tasks(), count_tasks()
'''

#my_code
class TodoList:
      def __init__(self, tasks: list):
           self.tasks = tasks
           
      def add_task(self, task):
            self.tasks.append(task)
            
      def remove_task(self, index : int):
            if (index < 0 or index >= len(self.tasks)):
                  print ("Index should be greater or equal to 0 but less than the length of the list.")
                  return
            
            del self.tasks[index]
            
      def show_tasks(self):
            return self.tasks
      
      def count_tasks(self):
            return len(self.tasks)
            
weekday_tasks = TodoList(["utho", "tayyar ho", "office jao", "ghar aao", "so jao"])  
sunday_tasks = TodoList(["mat utho", "pare raho", "duniya faani ha",  "hume neend pyari ha"])  
print(weekday_tasks.__dict__, sunday_tasks.__dict__, sep='\n')

sunday_tasks.add_task("raat ko jage raho")
weekday_tasks.remove_task(8)
print(weekday_tasks.__dict__, sunday_tasks.__dict__, sep='\n')

print(f'''
weekday_tasks.show_tasks() {weekday_tasks.show_tasks()}
sunday_tasks.show_tasks() {sunday_tasks.show_tasks()}
weekday_tasks.count_tasks() {weekday_tasks.count_tasks()}
sunday_tasks.count_tasks() {sunday_tasks.count_tasks()}
''')
