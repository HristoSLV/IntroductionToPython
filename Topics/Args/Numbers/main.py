# put your python code here
def multiply(*args):
    product = 1
    for number in args:
        print(args[number])
        product *= number
    return product


print(multiply(1, 2, 3))
