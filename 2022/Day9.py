import matplotlib.pyplot as plt
import math

with open('input9.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

x = y = 0
xt = yt = 0
coordinates = []
coordinatest = []


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


for c in lines:
    n = c.split()

    if n[0] == 'U':
        for i in range(int(n[1])):
            y += 1
            coordinates.append((x, y))
            if calculate_distance(x,y,xt,yt) <= math.sqrt(2):
                coordinatest.append((xt,yt))
            else:
                xt = x
                yt = y - 1
                coordinatest.append((xt,yt))

    if n[0] == 'D':
        for i in range(int(n[1])):
            y -= 1
            coordinates.append((x, y))
            if calculate_distance(x, y, xt, yt) <= math.sqrt(2):
                coordinatest.append((xt, yt))
            else:
                xt = x
                yt = y + 1
                coordinatest.append((xt, yt))

    if n[0] == 'L':
        for i in range(int(n[1])):
            x -= 1
            coordinates.append((x, y))
            if calculate_distance(x, y, xt, yt) <= math.sqrt(2):
                coordinatest.append((xt, yt))
            else:
                yt = y
                xt = x + 1
                coordinatest.append((xt, yt))

    if n[0] == 'R':
        for i in range(int(n[1])):
            x += 1
            coordinates.append((x, y))
            if calculate_distance(x, y, xt, yt) <= math.sqrt(2):
                coordinatest.append((xt, yt))
            else:
                yt = y
                xt = x - 1
                coordinatest.append((xt, yt))

print(len(set(coordinatest)))

def draw_coordinates(c):
    x_values = [coord[0] for coord in c]
    y_values = [coord[1] for coord in c]

    plt.plot(x_values, y_values, 'ro', markersize=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Coordinates')
    plt.grid(True)
    plt.show()


draw_coordinates(coordinatest)


