#Number guessing game
'''
1) user can give max n min range
2) user has limited chances based on the difficulty level EASY (more chance), MEDIUM (less chance, max rndm range), HARD(least chance, max rndm range)

'''
user_select = input("Choose 0-2 for easy-hard = ")
difficulty_levels = ["EASY", "MEDIUM", "HARD"]
rules_dict = {
      "EASY": {
            "chance": 5,
            "range": 5
            },
      "MEDIUM": {
            "chance": 3,
            "range": 15
            },
      "HARD": {
            "chance": 2,
            "range": 15
            }
}
print(("USER SELECTED", user_select))

if user_select.isdigit() and  (0 <= int(user_select) <= 2):
      user_integer = int(user_select)
      print("yes it is int")
      print(rules_dict[difficulty_levels[user_integer]])
      '''rest of the code'''
else:
      print("not an int")
