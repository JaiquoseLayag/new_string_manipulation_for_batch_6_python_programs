# Allow the user to input a string with leading spaces
string = input("Enter a string: ")
# Use a for loop to iterate through each charcter and check if it's a space
for i in range(len(string)):
    if string[i] != " ":
# Print the string once the first non-space character is found
# Break the loop