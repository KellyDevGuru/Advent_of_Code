with open('input7.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()[1:]]


class FileSystemNode:
    def __init__(self, name, is_file=False, size=0, parent=None):
        self.name = name
        self.is_file = is_file
        self.size = size
        self.children = []
        self.parent = parent  # Set the parent directory

    def add_child(self, child):
        self.children.append(child)

    def total_size(self):
        if self.is_file:
            return self.size
        else:
            return sum(child.total_size() for child in self.children)

def parse_file_system(input_data):
    root = FileSystemNode("/")
    current_dir = root

    for line in input_data:
        parts = line.split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    if current_dir.parent is not None:  # Check if not already at root
                        current_dir = current_dir.parent  # Move up to parent directory
                elif parts[2] == "/":
                    current_dir = root  # Move to root directory
                else:
                    for child in current_dir.children:
                        if child.name == parts[2]:
                            current_dir = child  # Move to specified child directory
                            break
            else:
                continue
        elif parts[0] == "dir":
            new_dir = FileSystemNode(name=parts[1])
            current_dir.add_child(new_dir)
            new_dir.parent = current_dir  # Set the parent directory
        else:
            current_dir.add_child(FileSystemNode(name=parts[1], is_file=True, size=int(parts[0])))

    return root


def find_directories_under_size(node, threshold):
    result = []
    if not node.is_file and node.total_size() <= threshold:
        result.append(node)
    for child in node.children:
        result.extend(find_directories_under_size(child, threshold))
    return result


# Parse the input to build the file system tree
root_node = parse_file_system(lines)

# Find directories with total size at most 100000
directories_under_threshold = find_directories_under_size(root_node, 100000)

# Calculate the sum of the total sizes of those directories
sum_of_sizes = sum(directory.total_size() for directory in directories_under_threshold)

print("Sum of total sizes of directories under 100000:", sum_of_sizes)
