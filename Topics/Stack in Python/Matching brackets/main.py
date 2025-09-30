expression = input()

stack = []

for char in expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if stack:
            stack.pop()
        else:
            print('ERROR')
            break
else:
    if stack:
        print('ERROR')
    else:
        print('OK')
