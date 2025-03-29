# Allow the user to input a string
string = input("Enter a string: ")
# Use a loop and check the ASCII values of each letter
# Return true if character is within a-z
for character in string:
    if 'A' <= character <= 'Z':
        print("False")
        break
else:
    print("True")