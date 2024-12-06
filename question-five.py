# Program to store a list of words and create a new list with words having odd number of characters
def odd_length_words():
    words = input("Enter a list of words separated by spaces: ").split()
    odd_words = [word for word in words if len(word) % 2 != 0]
    print(f"Words with odd number of characters: {odd_words}")

odd_length_words()