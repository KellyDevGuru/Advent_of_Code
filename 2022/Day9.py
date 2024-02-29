import math

with open('input9.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

x = y = 0
xt = yt = 0
coordinates = []
coordinatest = []

for c in lines:

    if c[0] == 'U':
        for i in range(int(c[2])):
            coordinates.append((x, (y + i + 1)))
            if x == xt:
                coordinatest.append((xt, (yt + i)))
            else:
                xt = x
                coordinatest.append((xt, (yt + i)))
        y += int(c[2])
        yt += (int(c[2]) - 1)

    if c[0] == 'D':
        for i in range(int(c[2])):
            coordinates.append((x, (y - i - 1)))
            if x == xt:
                coordinatest.append((xt, (yt - i)))
            else:
                xt = x
                coordinatest.append((xt, (yt - i)))

        y -= int(c[2])
        yt -= (int(c[2]) - 1)

    if c[0] == 'L':
        for i in range(int(c[2])):
            coordinates.append(((x - i - 1), y))
            if y == yt:
                coordinatest.append(((xt - i), yt))
            else:
                yt = y
                coordinatest.append(((xt - i), yt))

        x -= int(c[2])
        xt -= (int(c[2]) - 1)

    if c[0] == 'R':
        for i in range(int(c[2])):
            coordinates.append(((x + i + 1), y))
            if y == yt:
                coordinatest.append(((xt + i), yt))
            else:
                yt = y
                coordinatest.append(((xt + i), yt))
        x += int(c[2])
        xt += (int(c[2]) - 1)

print(len(set(coordinatest)))
