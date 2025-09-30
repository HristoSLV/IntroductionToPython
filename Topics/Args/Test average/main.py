def average_mark(*marks):
    total = sum(marks)
    average = total / len(marks)
    return round(average, 1)
