with open('input10.txt', 'r') as file:
    program = [x.strip() for x in file.readlines()]

v = 1
index = 0
signal_strength = []


for x in program:
    if x == 'noop':
        index += 1
        if index in [20, 60, 100, 140, 180, 220]:
            signal_strength.append(index * v)
    else:
        _, number = x.split()
        for i in range(2):
            index += 1
            if index in [20, 60, 100, 140, 180, 220]:
                signal_strength.append(index * v)
            if i == 1:
                v += int(number)

print(sum(signal_strength))


for x in program:
    if x == 'noop':
        index += 1
        row = ((index - 1) / 40)
        column = ((index - 1) % 40)


# PART 2
register = 1
cycle = 1
i = 0
screen = ""
first = True
while i < len(program):

    if register <= cycle % 40 <= register + 2:
        screen += "#"
    else:
        screen += "."

    if program[i][:4] == "addx":
        if not first:
            register += int(program[i][4:])
            i += 1
        first = not first
    else:
        i += 1
    cycle += 1

for pos, pixel in enumerate(screen, 1):
    if pos % 40 > 0:
        print(pixel, end="")
    else:
        print(pixel)


