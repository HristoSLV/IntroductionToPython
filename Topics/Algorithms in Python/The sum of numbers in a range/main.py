def range_sum(numbers, start, end):
    sum_numbers = 0
    for num in numbers:
        if start <= num <= end:
            sum_numbers += num
    return sum_numbers


input_numbers = list(map(int, input().split()))
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
