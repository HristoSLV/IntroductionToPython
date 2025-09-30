def check_number_type(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")


input_number = int(input())
check_number_type(input_number)
