with open('input5.txt', 'r') as file:
    stack, instructions = [part.split("\n") for part in file.read().split("\n\n")]

# Find pile number for letter
for line in stack:
    new_line = "  " + line
    for x in new_line:
        if x.isalpha():
            pile = (new_line.index(x) // 4) + 1
            print(pile)