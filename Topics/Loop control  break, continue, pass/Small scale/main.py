my_list = []

while True:
    my_input = input()
    if my_input == ".":
        break
    my_list.append(float(my_input))


print(min(my_list))
