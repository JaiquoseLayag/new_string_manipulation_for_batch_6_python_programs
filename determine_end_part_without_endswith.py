# Allow the user to input a string and the suffix
string = input("Enter a string: ")
suffix = input("Enter the suffix: ")
# Get the length of the suffix and slice the main string
length = len(suffix)
end_part = string[-length]
# Print True or False if the end part and suffix are the same or not