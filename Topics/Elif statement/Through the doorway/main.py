a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())

if a <= x and b <= y or c <= y:
    print("The box can be carried")
elif a <= y and b <= x or c <= x:
    print("The box can be carried")
else:
    print("The box cannot be carried")