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

print(stacks)
