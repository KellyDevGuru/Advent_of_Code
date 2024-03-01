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
