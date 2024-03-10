from collections import deque

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


def bfs(start, end, graph):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        visited.add(current)
        for neighbor in neighbours(current, graph):
            if graph[current] == 'S':
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
            elif neighbor not in visited and ord(graph[neighbor]) <= (ord(graph[current]) + 1):
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None


path = bfs(start_point, end_point, grid)
if path:
    print("Path found for Part 1:", path)
    print(len((path)))
else:
    print("No path found.")
