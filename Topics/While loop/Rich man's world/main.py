deposit = int(input())
interest = 1.071
years = 0

while deposit < 700_000:
    deposit *= interest
    years += 1

print(years)
