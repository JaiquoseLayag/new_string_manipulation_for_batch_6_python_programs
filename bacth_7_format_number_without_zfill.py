# Allow the user to input a number and desired length
number = int(input("Enter a number: "))
desired_length = int(input("Enter the desired length: "))
# Manually add zeroes before the number by taking its length
length = len(str(number))

if length < desired_length:
    zeroes = "0" * (desired_length - length)
    formatted_number = zeroes + str(number)
else:
    formatted_number = str(number)  
# Print result
print(formatted_number)
