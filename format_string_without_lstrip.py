# Allow the user to input a string with leading spaces
string = input("Enter a string: ")
# Use a for loop to iterate through each charcter and check if it's a space
for word in range(len(string)):
    if string[word] != " ":
# Print the string once the first non-space character is found
# Break the loop
        result = string[word:]
        break

print(result)