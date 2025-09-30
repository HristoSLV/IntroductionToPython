a = int(input())
b = int(input())

def are_same_object(a_, b_):
    if a_ is b_:
        return True
    else:
        return False

print(are_same_object(a, b))