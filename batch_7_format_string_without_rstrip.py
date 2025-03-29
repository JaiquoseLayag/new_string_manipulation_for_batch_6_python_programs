# Allow the user to input a string
string = input("Enter a string: ")
# Reverse iterate through each index for space characters
index = len(string) - 1
while index >= 0 and string[index] == " ":
    index -= 1
trimmed_text = string[:index + 1]
# Print from the start of the index up to the end of a non-space character