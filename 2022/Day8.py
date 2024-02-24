class Treetop:

    def __init__(self, size, coordinates):
        self.size = size
        self.x, self.y = coordinates

    def check_visibility(self, other_trees):
        for tree in other_trees:
            if tree.x == self.x and tree.y == self.y:
                continue  # Skip checking against itself
            if (tree.x == self.x and tree.y < self.y and tree.size > self.size) or \
               (tree.x == self.x and tree.y > self.y and tree.size > self.size) or \
               (tree.y == self.y and tree.x < self.x and tree.size > self.size) or \
               (tree.y == self.y and tree.x > self.x and tree.size > self.size):
                return False
        return True


with open('input8.txt', 'r') as file:
    content = [x.rstrip() for x in file.readlines()]


trees = []
for index_y, line in enumerate(content):
    for index_x, tree_size in enumerate(line):
        tree = Treetop(size=int(tree_size), coordinates=(index_x, index_y))
        trees.append(tree)


rows = (len(content) * 2) - 2
columns = (len(content[0]) * 2) - 2
edge_trees = rows + columns

visible_trees_count = 0
for tree in trees:
    if tree.check_visibility(trees):
        visible_trees_count += 1

print(f"Total number of visible trees: {visible_trees_count + edge_trees}")
