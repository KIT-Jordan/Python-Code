# Example of break statement
for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i reaches 3
    print(f"Number: {i}")

print("Loop finished!")  # This runs after the loop ends