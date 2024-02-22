with open('input8.txt', 'r') as file:
    content = [x.rstrip() for x in file.readlines()]


class Treetop:

    def __init__(self, size, coordinates, is_visible=False):
        self.size = size
        self.x, self.y = coordinates


trees = []
for index, line in enumerate(content):
    for indexc, char in enumerate(line):
        tree = Treetop(size=int(char), coordinates=(indexc, index))
        trees.append(tree)

