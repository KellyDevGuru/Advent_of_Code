with open('input9.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

x = y = 0
coordinates = []

for c in lines:

    if c[0] == 'D':
        for i in range(int(c[2])):
            coordinates.append((x, (y + i + 1)))
        y += int(c[2])

    if c[0] == 'U':
        for i in range(int(c[2])):
            coordinates.append((x, (y - i - 1)))
        y -= int(c[2])

    if c[0] == 'L':
        for i in range(int(c[2])):
            coordinates.append(((x - i - 1), y))
        x -= int(c[2])

    if c[0] == 'R':
        for i in range(int(c[2])):
            coordinates.append(((x + i + 1), y))
        x += int(c[2])

    # Update coordinate after each move
    coordinate = (x, y)
    print(coordinate)


for x in range(2):
    print(x)