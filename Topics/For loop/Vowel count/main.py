string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for char in vowels:
    for letter in string:
        if char == letter:
            counter += 1

print(counter)
