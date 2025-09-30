my_string = input()
# my_bool = True
#
# for i, char in range(0, len(my_string)):
#     if my_string[char] != my_string[len(my_string) - char - 1]:
#         my_bool = False
#
# if my_bool:
#     print("Palindrome")
# else:
#     print("Not palindrome")
#
# Both of these 2 versions work ~~~~~~

if my_string == my_string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
