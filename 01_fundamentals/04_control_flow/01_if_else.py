age = 18
x = 12
y = 23
z = 35

# PYTHON - Uses indentation (4 spaces recommended)
# if age >= 18:
#     print("You are an adult")
#     print("You can vote")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a child")

# Single line if (ternary-like)
status = "adult" if age >= 18 else "minor"
# print(status)

'''# Chained comparisons (PYTHON UNIQUE!)'''

if y > x < z:                       #no need to type "and" keyword python speciality
      print("running")

if type(age) is int and len(status) >= 2:
      print("All conditions true")

else:
      print(False)

