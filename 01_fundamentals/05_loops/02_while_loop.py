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
# num = 20
# while num >= 0:
#       num -= 1
#       if num == 4:
#             break
#       elif num % 2 == 0:
#             continue
#       else:
#             print(num)
      
'''while loop with complex condition'''
# import random
# attempts = 0
# max_attempts = 5
# while attempts < max_attempts and random.random() > 0.3:
#     print(f"Attempt {attempts + 1}")
#     attempts += 1
# else:
#     if attempts == max_attempts:
#         print("Max attempts reached")
#     else:
#         print("Condition met")

'''ex01
Write a program that prints the first 10 even numbers.'''
# count = 0
# current_even_num = 2
# while count < 10:
#       print(current_even_num)
#       count += 1
#       current_even_num += 2

'''ex02
Create a function that counts vowels and consonants in a string.'''
user_input = input("Enter Your Input Here: ")
processed_user_input = user_input.lower().strip()
vowels = 'aeiou'
consonant_count = 0
vowel_count = 0
char = 0

while char < len(processed_user_input):
      if processed_user_input[char].isalpha():
            if processed_user_input[char] in vowels:
                  vowel_count += 1
            else:
                  consonant_count +=1
      else:
            continue
      char += 1
print(vowel_count, consonant_count)
      