# place `import` statement at top of the program
import math

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))

reversed_x = math.copysign(x, y)
print(reversed_x)
