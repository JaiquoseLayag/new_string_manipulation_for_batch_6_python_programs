# Allow the user to input a string
string = input("Enter a string: ")
# Use a loop and check the ASCII values of each letter
# Return false if the value is greater than 90
for characters in string:
    if not ('A' <= characters <= 'Z'):
        print("False")
    else:
        print("True")
