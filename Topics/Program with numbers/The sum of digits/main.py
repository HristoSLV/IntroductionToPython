# put your python code here
three_digit_number = int(input())
first_digit = three_digit_number // 100
second_digit = three_digit_number // 10 % 10
third_digit = three_digit_number % 10
sum_of_digits = first_digit + second_digit + third_digit

print(sum_of_digits)
