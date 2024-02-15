with open('input1.txt', 'r') as file:
    content = [x.strip() for x in file]

res = 0
cal_list = []

for line in content:
    if line == '':
        cal_list.append(res)
        res = 0
    else:
        res += int(line)

print("Part 1:", max(cal_list))
