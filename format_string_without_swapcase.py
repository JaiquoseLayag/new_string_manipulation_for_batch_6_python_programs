# Allow the user to input a string
string = input("Enter a string: ")
# Use a loop and check for every uppercase and/or lowercase letter
# Add or subtract 32 to every ASCII code of each uppercase and/or lowercase letter
new_format = ""

for character in string:
    if 'A' <= character <= 'Z':
        new_format += chr(ord(character) + 32)
    elif 'a' <= character <= 'z':
        new_format += chr(ord(character) - 32)
    else:
        new_format += character
# Print result