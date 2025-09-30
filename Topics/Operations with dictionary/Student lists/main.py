# import operator
#
# write your code here
# student_list = {
#     "Math": ["Alice", "Ben", "Rihana"],
#     "Physics": ["Alice", "David"],
#     "History": ["Steve", "Charlie", "Jacky", "Britney", "Ben"]
# }

# # 1
# max_subject = max(student_list, key=lambda x: len(student_list[x]))
# print("1", max_subject)
#
# # 2
# print("2", max(student_list.items(), key=operator.itemgetter(1))[0])
#
# # 3
student_list_new = {key: len(value) for (key, value) in student_list.items()}
print(max(student_list_new, key=student_list_new.get))
