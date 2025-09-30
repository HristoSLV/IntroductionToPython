def sum_of_square_digits(n):
    # The input 'n' is a positive integer.
    # Convert the integer 'n' to a string to iterate over the digits.
    total = 0
    for digit in str(n):
        # For each digit, convert it back to integer and calculate its square.
        total += int(digit) ** 2
    # Add the square to a running total.
    # Return the total.
    return total


n = int(input())
print(sum_of_square_digits(n))
