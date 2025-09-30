# put your python code here
a = int(input())
b = int(input())
sum_divisible_by_3 = 0
count_divisible_by_3 = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sum_divisible_by_3 += i
        count_divisible_by_3 += 1

mean = sum_divisible_by_3 / count_divisible_by_3
print(mean)
