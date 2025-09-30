for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# fizz = "Fizz"
# buzz = "Buzz"
#
# for i in range(1, 101):
#     output = ""
#     if i % 3 == 0:
#         output += fizz
#     if i % 5 == 0:
#         output += buzz
#     print(output or i)
