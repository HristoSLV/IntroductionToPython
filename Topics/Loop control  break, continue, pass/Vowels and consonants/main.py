user_input = input()
vowels = 'aeiou'

for char in user_input:
    if char.isalpha():
        if char in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
