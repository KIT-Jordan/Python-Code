# Nested loops example - multiplication table
for i in range(1, 4):  # Outer loop
    print(f"\nMultiplication table for {i}:")
    for j in range(1, 4):  # Inner loop
        print(f"{i} × {j} = {i * j}")

print("\nMultiplication tables finished!")  # This runs after all loops end