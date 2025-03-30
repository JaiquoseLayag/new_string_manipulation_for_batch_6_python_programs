# Get input from the user
# Initialize a count
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

count = 0

main_length = len(main_string)
sub_length = len(substring)
# Loop through the main string and check for matches
# Check if it matches the search substring
for i in range(main_length - sub_length + 1):  
    current_part = main_string[i:i + sub_length]
    
    
    if current_part == substring:
        count += 1  
        
# Print result
print(count)