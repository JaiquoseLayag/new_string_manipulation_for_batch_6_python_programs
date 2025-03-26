# Allow the user to input both a string and the prefix of the string
string = input("Enter a string: ")
prefix = input("Enter the prefix: ")
# Use startswith() to check if the string strats with the prefix
# Slice the string starting from the index without the prefix
# Print the string without the prefix