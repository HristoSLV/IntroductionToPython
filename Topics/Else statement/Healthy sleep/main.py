minimum_sleep = int(input())
maximum_sleep = int(input())
your_sleep = int(input())

if minimum_sleep <= your_sleep <= maximum_sleep:
    print("Normal")
elif minimum_sleep > your_sleep:
    print("Deficiency")
else:
    print("Excess")
