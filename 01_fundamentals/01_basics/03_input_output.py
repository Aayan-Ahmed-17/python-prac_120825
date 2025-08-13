'''
input() takes inputs as a string
print() gives output as a string
'''


# type conversions of input() 
# user_age = int(input("Enter your age..."))
# height = float(input("Enter your height..."))

# a,b = input("enter something").split()                #two vals reqd not more or less to prevent errs   
# print(a,b, sep='|')


name = 'Alice'
age = 23
strike_rate = 130

print(f"Name: {name}, Age: {age}, Score: {strike_rate : .1f}")          # .1f use to show only a single digit after decimal
