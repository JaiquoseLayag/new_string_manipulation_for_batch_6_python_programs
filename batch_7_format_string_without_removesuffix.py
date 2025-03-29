# Allow the user to input a string and a suffix
string = input("Enter a string: ")
suffix = input("Enter the suffix used: ")
# Use endswith() to check if the string ends with the suffix
# Slice the string starting from the index without the suffix
if string.endswith(suffix):
    length = len(suffix)
    
    new_string = string[:len(string) - length] 
# Print result