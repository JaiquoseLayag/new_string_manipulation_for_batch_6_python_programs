# Allow the user to input string and desired length
string = input("Enter a string: ")
desired_length = int(input("Enter your desired length: "))
# Calculate how many spaces to be added to the left and right of the string
length = len(string)
if length < desired_length:
    total_spaces = desired_length - length
    left_space = total_spaces // 2
    right_space = total_spaces - left_space
# Manually add spaces to the left and right of the string
# Print result