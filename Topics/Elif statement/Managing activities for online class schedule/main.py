# The program starts here

def activity(day):
    # Use elif to set conditions for days of the week
    # Remember, the days are represented as follows:
    # 0 to 4 for Monday to Friday respectively
    # 5 for Saturday
    # 6 for Sunday
    # Write your code here!
    if 0 <= day <= 6:
        if 0 <= day <= 4:
            return "Study!"
        elif day == 5:
            return "Rest!"
        return "Leisure!"
    return "Invalid Input"


# Do not change anything below!

current_day = int(input())
print(activity(current_day))
