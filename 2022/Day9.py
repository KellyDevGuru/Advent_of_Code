import math

with open('input9.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

x = y = 0
coordinates = []

for c in lines:

    if c[0] == 'U':
        for i in range(int(c[2])):
            coordinates.append(((x, (y + i + 1)), c[0]))
        y += int(c[2])

    if c[0] == 'D':
        for i in range(int(c[2])):
            coordinates.append(((x, (y - i - 1)), c[0]))
        y -= int(c[2])

    if c[0] == 'L':
        for i in range(int(c[2])):
            coordinates.append((((x - i - 1), y), c[0]))
        x -= int(c[2])

    if c[0] == 'R':
        for i in range(int(c[2])):
            coordinates.append((((x + i + 1), y), c[0]))
        x += int(c[2])


def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance






