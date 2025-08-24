'''
->PY uses match case instead of switch case
->No need to use "break" as we use to do in Js
'''

day = 6
# match day:
#       case 1:
#             print("Monday")
#       case 2:
#             print("Tuesday")
#       case 3:
#             print("Wednesday")
#       case 4:
#             print("Thursday")
#       case 5:
#             print("Friday")
#       case 6:
#             print("Saturday")
#       case _:                                   # used as default case
#             print("Sunday")


# num = input("Enter your number here : ")
# match num:
#       case str() if int(num) > 0:                                 #Checks if the num is string if it is then this converts them into integer then compares them
#             print(f"Positive integer: {num}")
#       case str() if int(num) < 0:
#             print(f"Positive negative: {num}")
#       case str() if int(num) == 0:
#             print(f"Neither positive nor negative: {num}")

'''ex01 Basic Conditionals
Write a program that takes a number and prints whether it's positive, negative, or zero.
'''

# user_num = int(input("Enter your number here : "))
# match user_num:
#       case 0:
#             print(f"Neither negative nor positive integer: {user_num}")
#       case _ if user_num > 0:
#             print(f"Positive integer: {user_num}")
#       case _ if user_num < 0:
#             print(f"Negative integer: {user_num}")
#       case _ :
#             print(f"Invalid input: {user_num}")

'''ex02 Grade Calculator
Create a function that converts numeric grades to letter grades:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
'''
# user_score = int(input("Enter your score here : "))
# match user_score:
#       case _ if 90 <= user_score <= 100:
#             print(f"{user_score} is b/w 90-100 (A)")
#       case _ if 80 <= user_score <= 89:
#             print(f"{user_score} is b/w 80-89 (B)")
#       case _ if 70 <= user_score <= 79:
#             print(f"{user_score} is b/w 70-79 (C)")
#       case _ if 60 <= user_score <= 69:
#             print(f"{user_score} is b/w 60-69 (D)")
#       case _ if 0 <= user_score < 60:
#             print(f"{user_score} is less than 60 (F)")
#       case _ :
#             print(f"{user_score} Invalid! please enter number between 0 - 100")

