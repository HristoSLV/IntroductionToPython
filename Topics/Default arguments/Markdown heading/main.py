def heading(string, number=1):
    if number < 1:
        number = 1
    elif number > 6:
        number = 6
    return "#" * number + " " + string