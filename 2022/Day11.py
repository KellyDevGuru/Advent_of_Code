import re
from functools import reduce


with open('input11.txt', 'r') as file:
    content = [line for line in file.readlines()]


# Define the Monkey class
class Monkey:
    def __init__(self, number, items, worry_level, test, t, f):
        self.number = number
        self.items = items
        self.worry_level = worry_level
        self.test = test
        self.t = t
        self.f = f

    def throw_item(self, item):
        new_worry = (eval(re.sub(r'\bold\b', str(item), self.worry_level))) // 3
        if new_worry % self.test == 0:
            return self.t, new_worry
        else:
            return self.f, new_worry

    def receive_item(self, new_item):
        self.items.append(new_item)


# Initializing lists to store monkey data
monkeys = []

# Processing each line of content
for line in content:
    if 'Monkey' in line:
        number = int(line[7])  # Extracting the number after "Monkey"
    elif 'Starting' in line:
        numbers = re.findall(r'\b\d+\b', line)  # Using regex to find all numbers in the line
        items = [int(num) for num in numbers]
    elif 'Operation' in line:
        worry_level = line.split('=')[1].strip()  # Extracting and converting the number after '='
    elif 'Test' in line:
        test = int(re.search(r'\b\d+\b', line).group())  # Finding and converting the number using regex
    elif 'true' in line:
        t = int(re.search(r'\b\d+\b', line).group())  # Finding and converting the number using regex
    elif 'false' in line:
        f = int(re.search(r'\b\d+\b', line).group())  # Finding and converting the number using regex

    # If all attributes are retrieved, create a Monkey object and append it to the list
    if 'false' in line:
        monkey = Monkey(number=number, items=items, worry_level=worry_level, test=test, t=t, f=f)
        monkeys.append(monkey)

monkeys_dict = {monkey.number: monkey for monkey in monkeys}

inspected = 0
monkey_inspected = {}


for x in range(20):
    for monkey in monkeys_dict.values():
        for item in monkey.items:
            inspected += 1
            monkey_number, value = monkey.throw_item(item)
            monkeys_dict[monkey_number].receive_item(value)
            print(f"Monkey {monkey_number} received {value}")
        monkey.items = []
        print(f"Monkey {monkey.number} inspected {inspected} items after round {x}")
        # Initialize the count if the monkey number is not already in the dictionary
        if monkey.number not in monkey_inspected:
            monkey_inspected[monkey.number] = 0

        # Increment the count for the inspected items for the current monkey
        monkey_inspected[monkey.number] += inspected
        inspected = 0

# Part 1
two_monkeys = sorted(monkey_inspected.values(), reverse=True)[:2]
result = reduce(lambda x, y: x * y, two_monkeys)
print(result)
