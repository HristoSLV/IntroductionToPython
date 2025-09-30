from collections import deque

n = int(input())
stack = deque()
read_stack = deque()

for _ in range(n):
    action = input()
    parts = action.split(" ", 1)

    if parts[0] == "BUY":
        book_name = parts[1]
        stack.append(book_name)
    elif parts[0] == "READ":
        if stack:
            read_stack.append(stack.pop())

for book in read_stack:
    print(book)
