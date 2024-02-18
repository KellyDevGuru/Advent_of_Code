with open('input5.txt', 'r') as file:
    stack, instructions = [part.split("\n") for part in file.read().split("\n\n")]

stacks = []
# Append the letters to the pile
for line in stack:
    new_line = "  " + line
    for i, x in enumerate(new_line):
        if x.isalpha():  # Check if line contains letter
            pile = (i // 4) + 1  # Calculate corresponding pile number
            found = False
            for item in stacks:
                if item[0] == pile:  # Check if pile number already exists in stacks list
                    item[1].append(x)
                    found = True
                    break
            if not found:
                stacks.append([pile, [x]])


instructions.pop()  # Delete '' from the list

for line in instructions:
    _, amount, _, pile_before, _, pile_after = line.split(' ')
    pile_to_remove_from = sorted(stacks)[int(pile_before) - 1][1]
    pile_to_add_to = sorted(stacks)[int(pile_after) - 1][1]
    items = (pile_to_remove_from[:int(amount)])  # Items in the pile that should be removed
    for _ in range(int(amount)):
        pile_to_remove_from.pop(0)
    for x in reversed(items):  # Remove reversed() for solution of Part 1
        pile_to_add_to.insert(0, x)

print(sorted(stacks))