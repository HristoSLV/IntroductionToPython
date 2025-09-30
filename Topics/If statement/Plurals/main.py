number = int(input())
word = input()
plural = "s"

# write a condition for plurals
if number > 1:
    word += plural
elif number < 1:
    word += plural

print(number, word)
