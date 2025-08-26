# count = 0
# while count <= 5:
#       print(count)
#       count += 1                    #No ++ operator in py
      
'''While with else (unique to Python!)'''
# count = 4
# while count >= 0:
#       print(f"count = {count}")
#       count -= 1
# else:
#       print("While loop ended successfully")                #runs when loop wasn't broken
      
      
'''while loop with break n cont, if n elif'''
num = 20
while num >= 0:
      num -= 1
      if num == 4:
            break
      elif num % 2 == 0:
            continue
      else:
            print(num)
      