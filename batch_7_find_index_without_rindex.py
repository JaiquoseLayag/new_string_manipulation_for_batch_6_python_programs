# Allow the user to input a string
text = input("Enter the main string: ")
substring = input("Enter the substring to find: ")
# Loop through the string in reverse
text_length = len(text)
sub_length = len(substring)

found_index = -1

for i in range(text_length - sub_length, -1, -1):
    if text[i:i + sub_length] == substring:
        found_index = i
        break
# Print result