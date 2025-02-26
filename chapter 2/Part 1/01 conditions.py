# Define two variables for comparison == <= >= != > < 
a = 5
b = 3

# Check for equality (==)
print(f"a == b : {a == b}")  # False because 5 is not equal to 3

# Check for inequality (!=)
print(f"a != b : {a != b}")  # True because 5 is not equal to 3

# Check if a is less than b (<)
print(f"a < b : {a < b}")    # False because 5 is not less than 3

# Check if a is less than or equal to b (<=)
print
(f"a <= b : {a <= b}")  # False because 5 is not less than or equal to 3

# Check if a is greater than b (>)
print(f"a > b : {a > b}")    # True because 5 is greater than 3

# Check if a is greater than or equal to b (>=)
print(f"a >= b : {a >= b}")  # True because 5 is greater than or equal to 3

# Practical example using if statement
age = 25
if age >= 18:
    print("\nAge is sufficient for voting")  # This will be printed because 25 >= 18>