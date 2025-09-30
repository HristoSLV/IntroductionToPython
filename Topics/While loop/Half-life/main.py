def num2date(num):
    months = [(31, 'jan'), (28, 'feb'), (31, 'mar'), (30, 'apr'),
              (31, 'may'), (30, 'jun'), (31, 'jul'), (31, 'aug'),
              (30, 'sep'), (31, 'oct'), (30, 'nov'), (31, 'dec')]

    i = 0
    for i in range(11, -1, -1):
        if num > months[11-i][0]:
            num -= months[11-i][0]
        else:
            break

    return (num, months[11-i][1])

print(num2date(32))