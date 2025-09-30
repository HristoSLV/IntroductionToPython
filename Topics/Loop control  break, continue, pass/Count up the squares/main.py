# put your python code here
my_list = []
sum_nums = 0

while True:
    n = int(input())
    sum_nums += n
    my_list.append(n * n)
    if sum_nums == 0:
        print(sum(my_list))
        break
