# Allow the user to input a string and the first part of the string
string = input("Enter a string: ")
first_part = input("Enter the first part: ")
# Slice the string up to the first part
# Compare with the length of the first part
length = len(first_part)

if string[:length] == first_part:
# Print result