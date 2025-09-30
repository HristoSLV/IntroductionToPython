scores = input().split()
# put your python code here
correct = 0
wrong = 0

while True:
    for i in scores:
        if i == "C":
            correct += 1
        if i == "I":
            wrong += 1
            if wrong == 3:
                break
    if wrong == 3:
        print("Game over")
        print(correct)
        break
    if wrong < 3:
        print("You won")
        print(correct)
        break
