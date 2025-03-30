# Allow the user to input a string 
text = input("Enter a string: ")
char = input("Enter a character to find: ")
# Loop through the string and find the characters
found = False
for i in range(len(text)):
    if text[i] == char:
        print(i)
        found = True
        break
# Print result
if not found:
    print("Substring not found")