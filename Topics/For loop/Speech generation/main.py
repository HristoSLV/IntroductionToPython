digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

phone_number = input()

for char in phone_number:
    index = int(char)
    print(digits[index])
