def cartesian_coordinate_plane_locator(x, y):
    if x == 0 and y == 0:
        return "It's the origin!"
    elif x == 0 or y == 0:
        return "One of the coordinates is equal to zero!"
    elif x > 0:
        if y > 0:
            return "I"
        return "IV"
    elif y > 0:
        return "II"
    return "III"


x_input = float(input())
y_input = float(input())

location = cartesian_coordinate_plane_locator(x_input, y_input)
print(location)
