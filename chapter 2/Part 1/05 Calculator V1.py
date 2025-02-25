# print("Welcome to the calculator program \n")
# print("Enter the first number greater than 0 and less than 100\n")
# g =float(input("Enter the number: "))

# if g > 0 and g < 100:
#     print("Number is greater than 0 and less than 100")
#     if g > 90:
#         print("A")
#     elif g > 80:
#         print("B")
#     elif g > 70:
#         print("C")    
#     else:
#         print("F")


arr = [1,2,3,4,5,6,7,8,9,10]
g =float(input("Enter the number: "))
if g in arr:
    print("Number is in the list")




# # Get the first number from user
# num1 = float(input("Enter first number: "))

# # Get the operator from user
# operator = input("Enter operator (+, -, *, /): ")

# # Get the second number from user
# num2 = float(input("Enter second number: "))


# # Check for addition
# if operator == "+":
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")
    
# # Check for subtraction
# elif operator == "-":
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")
        
# # Check for multiplication
# elif operator == "*":
#     result = num1 * num2
#     print(f"{num1} * {num2} = {result}")
            
# # Check for division
# elif operator == "/":
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# else:
#     # Handle invalid operator
#     print("Invalid operator! Please use +, -, *, or /")