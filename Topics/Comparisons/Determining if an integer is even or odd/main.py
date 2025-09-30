def determine_even_odd(n):
    # Placeholder for your code. You need to write the code to determine if the number is even or odd.
    # You need to ignore the sign of the number.
    # Return 'even' if the number is even and 'odd' if the number is odd.
    if n % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
    return is_even


# start of your code

input_number = int(input())
print(determine_even_odd(input_number))
