with open('input4.txt', 'r') as file:
    content = [x.strip() for x in file]


res = 0
res2 = 0
for line in content:
    pairs = line.split(",")
    first_pair_firstno = pairs[0].split("-")[0]
    first_pair_secondno = pairs[0].split("-")[1]
    second_pair_firstno = pairs[1].split("-")[0]
    second_pair_secondno = pairs[1].split("-")[1]

    first_pair = [x for x in range(int(first_pair_firstno), int(first_pair_secondno) + 1)]
    second_pair = [x for x in range(int(second_pair_firstno), int(second_pair_secondno) + 1)]

    # Part 1
    # if all(elem in first_pair for elem in second_pair) or all(elem in second_pair for elem in first_pair):
    #     res +=1

    if set(first_pair).intersection(set(second_pair)):
        res2 += 1

print("Part 1:", res)
print("Part 2:", res2)