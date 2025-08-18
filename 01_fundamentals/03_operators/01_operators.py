'''
ARITHMETIC OPERATORS
'''

# a = int(input("enter your first number"))
# b = int(input("enter your second number"))

# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b 
# floor_division = a // b
# modulus = a % b
# expontentional = a ** b

# print(f"{a} + {b}: addition: {addition}" )
# print(f"{a} - {b}: subtraction: {subtraction}" )
# print(f"{a} * {b}: multiplication: {multiplication}" )
# print(f"{a} / {b}: division: {division}" )
# print(f"{a} // {b}: floor_division: {floor_division}" )
# print(f"{a} % {b}: modulus: {modulus}" )
# print(f"{a} ** {b}: expontentional: {expontentional}" )     


'''
COMPARISION OPERATORS
'''
# print(1 == "1")               #false
# print(2 != 1)                   #true
# print(4 < 5 )                   #true
# print(True > False)         #true
# print("hi" <= "hello")     #false
# print("2" >= "2")            #true  | both side str needed if want to compare else print(2 >= "2") TypeError: '>=' not supported between instances of 'int' and 'str')

'''
LOGICAL OPERATORS
'''
# print(True and True)               #f
# print(False and True)               #f   
# print(True and False)               #f   
# print(True or True)                  #T
# print(False or True)                  #T
# print(False or False)                  #F
# print(not True)                         #f
# print(not False)                        #T

'''
ASSIGNMENT OPERATORS
=   # Basic assignment
+=  # Add and assign
-=  # Subtract and assign
*=  # Multiply and assign
/=  # Divide and assign
//= # Floor divide and assign
%=  # Modulus and assign
**= # Exponent and assign
'''   

basic_opr =   2                     #simply assigning value
print(basic_opr)
basic_opr += 4                    #basic_opr = basic_opr + 4
print(basic_opr)
basic_opr -= 3                     # subtractin 3 from basic_opr (6)
print(basic_opr)
basic_opr *= 5                      #multiplyin 5 with 3
print(basic_opr)
basic_opr /= 3                      #dividin 3  by 15
print(basic_opr)
basic_opr //= 2                     # divide then floor to real num 
print(basic_opr)
basic_opr %= 1                     # divin modulus of 2 by 1 which is 0
print(basic_opr)
basic_opr **= 4                     # 0 ** 4
print(basic_opr)

