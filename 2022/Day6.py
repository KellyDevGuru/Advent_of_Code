with open('input6.txt', 'r') as file:
    line = file.read()

chars = [x for x in line[0:4]]
for index, x in enumerate(line[4:]):
    if len(set(chars)) == 4:
        print("Part 1:", index + 4)  # Add 4 to index because enumerate starts at index 4
        break
    else:
        chars.append(x)
        del chars[0]

