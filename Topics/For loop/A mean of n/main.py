n = int(input())
sum_list = 0

for _ in range(n):
    sum_list += int(input())

mean = sum_list / n
print(mean)


# numbers = int(input())
# numbers_list = []
#
# for _ in range(numbers):
#     n = int(input())
#     numbers_list.append(n)
# avg = sum(numbers_list) / len(numbers_list)
# print(float(avg))