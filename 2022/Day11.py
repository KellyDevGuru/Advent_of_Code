with open('input11.txt', 'r') as file:
    content = [x.strip() for x in file.readlines()]


class Monkey:

    def __init__(self, number, items, worry_level, test, t, f):
        self.number = number
        self.items = items
        self.worry_level = worry_level
        self.test = test
        self.t = t
        self.f = f

    def throw_item(self):
        new_worry = self.worry_level // 3

        if new_worry % self.test:
            return self.t
        else:
            return self.f


