def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32  # Convert Celsius to Fahrenheit
    elif unit == 'F':
        return (temp - 32) * 5/9  # Convert Fahrenheit to Celsius
    else:
        return "Invalid unit"

# Example usage
print(convert_temperature(100, 'C'))  # 212.0
print(convert_temperature(212, 'F'))  # 100.0