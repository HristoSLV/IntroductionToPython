# Read the user's age
input_age = int(input())
age_group_1 = "Senior"
age_group_2 = "Adult"
age_group_3 = "Minor"


# Check the age and print the corresponding category
# TODO: Write your if statement here
def age_group(age):
    if age > 64:
        return age_group_1
    elif age > 17:
        return age_group_2
    else:
        return age_group_3


print(age_group(input_age))
