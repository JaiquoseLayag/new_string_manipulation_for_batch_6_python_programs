# Allow the user to input a string
string = input("Enter a string: ")
# Use upper() on the first letter and lower() on the remaining letters
first_letter = string[0].upper()
remaining = string[1:].lower()

new_string = first_letter + remaining
# Print result