def analyze_text(text):
    words = text.split()
    letters = len(text.replace(" ", ""))
    return len(words), letters

# Example usage
text = "Hello, welcome to the world of programming!"
word_count, letter_count = analyze_text(text)
print(f"Number of words: {word_count}, Number of letters: {letter_count}")