import random

with open('input12.txt', 'r') as file:
    heightmap = [x.strip() for x in file]

start_point = (0, 20)
end_point = (136, 20)

grid = {}
for i_y, y in enumerate(heightmap):
    for i_x, x in enumerate(y):
        grid[i_x, i_y] = x


def neighbours(coordinate, dictionary):

    x, y = coordinate
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [p for p in candidates if p in dictionary]


def step_to(neighbours, coordinate, dictionary):
    possible_steps = []

    if coordinate == start_point:  # Handle starting point differently
        for n in neighbours:
            if ord('a') + 1 <= ord(dictionary[n]):
                possible_steps.append(n)

    else:
        for n in neighbours:
            if ord(dictionary[coordinate]) + 1 <= ord(dictionary[n]):
                possible_steps.append(n)

    return random.choice(possible_steps)


next_step = None

while next_step != (136, 20):
    nearby_neighbors = neighbours(start_point, grid)
    if start_point == (137, 20):
        break  # Step out of while if start_point is on coordinate with letter 'z'
    next_step = step_to(nearby_neighbors, start_point, grid)
    start_point = next_step
    print(next_step)
