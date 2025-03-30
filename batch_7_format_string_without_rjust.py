# Allow the user to input a string and the desired length
string = input("Enter a string: ")
desired_length = int(input("Enter the desired length: "))
# Manually add spaces if the length of string is shorter than the desired length
length = len(string)

if length < desired_length:
    count = desired_length - length
    count = " " * count
    new_string = count + string
else:
    new_string = string
# Print result
print(new_string)