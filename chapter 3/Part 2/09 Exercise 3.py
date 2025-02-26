def check_word(text, word):
    return word in text

# Example usage
text = "Hello, World!"
print(check_word(text, "World"))  # True
print(check_word(text, "Python")) # False