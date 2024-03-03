import re

with open('input11.txt', 'r') as file:
    content = [line for line in file.readlines()]


# Define the Monkey class
class Monkey:
    def __init__(self, number, items, worry_level, test, t, f):
        self.number = number
        self.items = items
        self.worry_level = eval(re.sub(r'\bold\b', str(items[0]), worry_level))
        self.test = test
        self.t = t
        self.f = f

    def throw_item_to(self):
        self.items.pop(0)
        new_worry = self.worry_level // 3
        if new_worry % self.test:
            return self.t, new_worry
        else:
            return self.f, new_worry


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




