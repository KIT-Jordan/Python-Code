print("Welcome to the calculator program ")

# Get the first number from user
num1 = float(input("Enter first number: "))

# Get the operator from user
operator = input("Enter operator (+, -, *, /): ")

# Get the second number from user
num2 = float(input("Enter second number: "))


# Check for addition
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    
# Check for subtraction
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
        
# Check for multiplication
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
            
# Check for division
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    # Handle invalid operator
    print("Invalid operator! Please use +, -, *, or /")