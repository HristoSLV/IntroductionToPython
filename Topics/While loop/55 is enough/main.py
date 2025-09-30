# put your code here
sum_input = 0
total_numbers = 0
average_input = 0
number = 0

while number != 55:
    user_input = int(input())
    if user_input != 55:
        sum_input += user_input
        total_numbers += 1
    number = user_input

average_input = sum_input / total_numbers
print(total_numbers)
print(sum_input)
print(round(average_input))
