angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

if angle_1 != 0 and angle_2 != 0 and angle_3 != 0:
    if angle_1 + angle_2 + angle_3 == 180:
        print("The triangle is valid!")
    else:
        print("The triangle is not valid!")

else:
    print("The triangle is not valid!")
