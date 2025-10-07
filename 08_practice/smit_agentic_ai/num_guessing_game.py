#Number guessing game
'''
1) user can give max n min range
2) user has limited chances based on the difficulty level EASY (more chance), MEDIUM (less chance, max rndm range), HARD(least chance, max rndm range)

'''
difficulty_levels = ["EASY", "MEDIUM", "HARD"]

user_select = int(input("Choose 0-2 for easy-hard = "))
print(("USER SELECTED", user_select))
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

print(rules_dict[difficulty_levels[user_select]])