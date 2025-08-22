age = 18

# PYTHON - Uses indentation (4 spaces recommended)
if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Single line if (ternary-like)
status = "adult" if age >= 18 else "minor"
print(status)