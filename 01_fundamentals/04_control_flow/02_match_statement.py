'''
->PY uses match case instead of switch case
->No need to use "break" as we use to do in Js
'''

day = 6

match day:
      case 1:
            print("Monday")
      case 2:
            print("Tuesday")
      case 3:
            print("Wednesday")
      case 4:
            print("Thursday")
      case 5:
            print("Friday")
      case 6:
            print("Saturday")
      case _:                                   # used as default case
            print("Sunday")