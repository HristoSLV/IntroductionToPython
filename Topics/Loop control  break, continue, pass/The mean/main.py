my_sum = 0
counter = 0

while True:
    user_input = input()
    if user_input == ".":
        break
    else:
        my_sum += int(user_input)
        counter += 1

mean = my_sum / counter
print(mean)
