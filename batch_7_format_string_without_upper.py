# Allow the user to input a string
string = input("Enter a string: ")
# Use a loop and check for every lowercase letter 
uppercase_format = ""

for characters in string:
    if 'a' <= characters <= 'z':
# Subtract 32 to every ASCII code of each lowercase letter
# Print result

        uppercase_format += chr(ord(characters) - 32)
    else:
        uppercase_format += characters

print(uppercase_format)