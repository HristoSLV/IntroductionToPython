# Get the input integer from the user
number = int(input())

# Initialize the sum variable to 0
sum_numbers = 0

# Iterate from 1 to the input integer (inclusive)
# Square the current number
for i in range(0, number + 1):
    sum_numbers += i ** 2

# Add the squared number to the sum

# Print the final sum
print(sum_numbers)
