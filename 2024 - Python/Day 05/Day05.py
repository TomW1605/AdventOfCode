import time

from readFile import readFile

class Rule:
    def __init__(self, page_1: str, page_2: str):
        self.page_1 = page_1
        self.page_2 = page_2

    def __str__(self):
        return f"Rule({self.page_1}, {self.page_2})"

    def __repr__(self):
        return self.__str__()

    def check(self, update: list[str]):
        if self.page_1 in update and self.page_2 in update:
            return update.index(self.page_1) < update.index(self.page_2)
        return True

    def apply(self, update: list[str]):
        if not self.check(update) and self.page_1 in update and self.page_2 in update:
            index_1 = update.index(self.page_1)
            index_2 = update.index(self.page_2)
            update[index_1], update[index_2] = update[index_2], update[index_1]
        return update

def filter_updates(input_lines):
    rules_str, updates_str = "\n".join(input_lines).split("\n\n")
    rules = [Rule(*rule.split("|")) for rule in rules_str.split("\n")]
    updates = [update.split(',') for update in updates_str.split("\n")]

    valid_updates = []
    invalid_updates = []
    for update in updates:
        valid_update = True
        for rule in rules:
            if not rule.check(update):
                valid_update = False
                break
        if valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates, rules

def part1(input_lines):
    valid_updates = filter_updates(input_lines)[0]

    total = 0
    for update in valid_updates:
        total += int(update[int((len(update) - 1)/2)])
    print(total)

def part2(input_lines):
    _, invalid_updates, rules = filter_updates(input_lines)

    for update in invalid_updates:
        valid_update = False
        while not valid_update:
            valid_update = True
            for rule in rules:
                rule.apply(update)
            for rule in rules:
                if not rule.check(update):
                    valid_update = False
                    break

    total = 0
    for update in invalid_updates:
        total += int(update[int((len(update) - 1)/2)])
    print(total)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
