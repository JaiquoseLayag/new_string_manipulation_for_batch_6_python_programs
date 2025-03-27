# Allow the user to input a string
string = input("Enter a string: ")
# Use split() to separate each word
# Use upper() and lower() on the first and remaining letters
split = string.split()
words = []

for word in split:
    first_letter = word[0].upper()
    remaining = word[1:].lower()
    new_words = first_letter + remaining
    words.append(new_words)
# Use join() to add all new words together
# Print result
new_string = " ".join(words)

print(new_string)