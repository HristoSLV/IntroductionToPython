# Import statements


def square(num):
    # Function to square a number
    global result
    result = num ** 2


def main():
    # Get user input
    num = int(input())

    # Call the square function
    square(num)


    # Print the result
    print(result)


if __name__ == "__main__":
    main()