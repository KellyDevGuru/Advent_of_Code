class Treetop:

    def __init__(self, size, coordinates):
        self.size = size
        self.x, self.y = coordinates

    def get_viewing_distance(self, other_trees):
        # Initialize viewing distances
        up_distance = down_distance = left_distance = right_distance = 0

        trees_left = [t for t in other_trees if t.y == self.y and t.x < self.x]
        trees_right = [t for t in other_trees if t.y == self.y and t.x > self.x]
        trees_up = [t for t in other_trees if t.x == self.x and t.y < self.y]
        trees_down = [t for t in other_trees if t.x == self.x and t.y > self.y]

        for t in reversed(trees_left):
            if t.size == self.size:
                left_distance += 1
                break
            if t.size > self.size:
                break
            left_distance += 1

        for t in trees_right:
            if t.size == self.size:
                right_distance += 1
                break
            if t.size > self.size:
                break
            right_distance += 1

        for t in reversed(trees_up):
            if t.size == self.size:
                up_distance += 1
                break
            if t.size > self.size:
                break
            up_distance += 1

        for t in trees_down:
            if t.size == self.size:
                down_distance += 1
                break
            if t.size > self.size:
                break
            down_distance += 1

        return left_distance, right_distance, up_distance, down_distance

    def check_visibility(self, other_trees):
        if self.x == 0 or self.x == 98 or self.y == 0 or self.y == 98:
            return True  # Trees on the border are always visible

        # Initialize lists for trees in the same row and column
        row_trees = [tree for tree in other_trees if tree.y == self.y]
        col_trees = [tree for tree in other_trees if tree.x == self.x]

        # Check visibility in each direction
        left_visible = all(tree.size < self.size for tree in row_trees if tree.x < self.x)
        right_visible = all(tree.size < self.size for tree in row_trees if tree.x > self.x)
        up_visible = all(tree.size < self.size for tree in col_trees if tree.y < self.y)
        down_visible = all(tree.size < self.size for tree in col_trees if tree.y > self.y)

        # Return True only if at least one direction is visible
        return up_visible or down_visible or left_visible or right_visible

with open('input8.txt', 'r') as file:
    content = [x.rstrip() for x in file.readlines()]

trees = []
for index_y, line in enumerate(content):
    for index_x, tree_size in enumerate(line):
        tree = Treetop(size=int(tree_size), coordinates=(index_x, index_y))
        trees.append(tree)

visible_trees_count = 0
for tree in trees:
    if tree.check_visibility(trees):
        visible_trees_count += 1

score = 0
scores = []

for tree in trees:
    left, right, up, down = tree.get_viewing_distance(trees)
    score = left * right * up * down
    scores.append(score)

print(f"Highest scenic score possible: {max(scores)}")

print(f"Total number of visible trees: {visible_trees_count}")

