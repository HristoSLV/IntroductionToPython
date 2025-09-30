# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
number_of_groups = int(input())
groups_dict = dict.fromkeys(groups)
# counter = 1
#
# for key in groups_dict:
#     if counter > number_of_groups:
#         break
#     try:
#         value = input()
#         groups_dict[key] = int(value)
#         counter += 1
#     except ValueError:
#         print("Something went wrong")
#
# print(groups_dict)


groups_dict.update({groups[index]: int(input()) for index in range(number_of_groups)})

print(groups_dict)
