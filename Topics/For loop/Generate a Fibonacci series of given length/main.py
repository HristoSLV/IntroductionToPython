# Function to generate a fibonacci sequence
def generate_fib_sequence(n):
    # Create an empty list
    sequence = []
    a = 0
    b = 1

    # Your logic here
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    # Finally, return the sequence
    return sequence


# Get the length of the sequence from the user.
seq_length = int(input())

# Call the function and print the sequence.
# my_string = " ".join(str(number) for number in generate_fib_sequence(seq_length))
# print(my_string)
# print(generate_fib_sequence(seq_length))
print(*generate_fib_sequence(seq_length))
