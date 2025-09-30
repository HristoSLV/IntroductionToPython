# put your python code here
students_1 = int(input())
students_2 = int(input())
students_3 = int(input())

desks_1 = (students_1 // 2) + (students_1 % 2)
desks_2 = (students_2 // 2) + (students_2 % 2)
desks_3 = (students_3 // 2) + (students_3 % 2)

total_desks = desks_1 + desks_2 + desks_3
print(total_desks)
