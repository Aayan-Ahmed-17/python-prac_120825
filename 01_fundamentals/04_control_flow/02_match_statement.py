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

num = input("Enter your number here : ")

match num:
      case str() if int(num) > 0:                                 #Checks if the num is string if it is then this converts them into integer then compares them
            print(f"Positive integer: {num}")
      case str() if int(num) < 0:
            print(f"Positive negative: {num}")
      case str() if int(num) == 0:
            print(f"Neither positive nor negative: {num}")