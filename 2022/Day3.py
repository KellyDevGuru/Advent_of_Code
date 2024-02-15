with open('input3.txt', 'r') as file:
    content = [x.strip() for x in file.readlines()]


def get_priority(item_type):
    item_type = item_type.pop()

    if 'a' <= item_type <= 'z':
        return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z':
        return ord(item_type) - ord('A') + 27

#Part 1
result = 0
for line in content:
    similar = set(line[:(len(line)//2)]).intersection(set(line[(len(line)//2):]))
    x = get_priority(similar)
    result += x

#Part2
groups = [content[i:i+3] for i in range(0, len(content), 3)]
result2 = 0
for x in groups:
    similar = set(x[0]).intersection(set(x[1]), set(x[2]))
    x = get_priority(similar)
    result2 += x

print("Part 1:", result)
print("Part 2:", result2)