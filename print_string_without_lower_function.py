# Allow the user to input a string
string = input("Enter a string: ")
# Use a loop and check for every uppercase letter 
lowercase_format = ""

for characters in string:
    if 'A' <= character <= 'Z':
# Add 32 to every ASCII code of each uppercase letter
        lowercase_format += chr(ord(characters) + 32)
    else:
        lowercase_format += characters
# Print result
print(lowercase_format)