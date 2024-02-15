with open('input2.txt', 'r') as file:
    content = [x.rstrip() for x in file]

# part 1
points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

points2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

print(f"Part 1: {sum([points[round] for round in content])}")
print(f"Part 2: {sum([points2[round] for round in content])}")