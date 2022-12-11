from readFile import readFile

class Monkey:
    id = 0
    items = []
    operation = lambda self, old: old
    test_val = 1
    true_monkey = None
    false_monkey = None
    inspect_count = 0

    def __init__(self, ID):
        self.id = ID

    def __str__(self):
        return f"Monkey {self.id}:\n  Starting items: {self.items}\n  Test: divisible by {self.test_val}\n    If true: throw to monkey {self.true_monkey.id}\n    If false: throw to monkey {self.false_monkey.id}"

    def __repr__(self):
        return f"Monkey {self.id} inspected items {self.inspect_count} times."

def part1(input_lines):
    print(input_lines)
    new_monkeys = [new_monkey_text.split("\n") for new_monkey_text in "\n".join(input_lines).split("\n\n")]
    print(new_monkeys)
    monkeys = [Monkey(ii) for ii in range(len(new_monkeys))]

    for ii in range(len(monkeys)):
        monkey = monkeys[ii]
        new_monkey = new_monkeys[ii]
        monkey.items = [int(item) for item in new_monkey[1].lstrip("  Starting items: ").split(", ")]
        monkey.operation = eval(f"lambda old: {new_monkey[2].split(' = ')[1]}")
        monkey.test_val = int(new_monkey[3].split(" ")[-1])
        monkey.true_monkey = monkeys[int(new_monkey[4].split(" ")[-1])]
        monkey.false_monkey = monkeys[int(new_monkey[5].split(" ")[-1])]

    print("\n\n".join([str(monkey) for monkey in monkeys]))

    print("------------------------------------------")
    print("\n".join([monkey.__repr__() for monkey in monkeys]))

    for ii in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspect_count += 1
                item = monkey.operation(item)
                item = int(item/3)
                if item % monkey.test_val == 0:
                    monkey.true_monkey.items.append(item)
                else:
                    monkey.false_monkey.items.append(item)
            monkey.items.clear()

        print("------------------------------------------")
        print(f"After round {ii+1}")
        print("\n".join([monkey.__repr__() for monkey in monkeys]))

    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    print(monkeys[0].inspect_count*monkeys[1].inspect_count)

def part2(input_lines):
    print(input_lines)
    new_monkeys = [new_monkey_text.split("\n") for new_monkey_text in "\n".join(input_lines).split("\n\n")]
    print(new_monkeys)
    monkeys = [Monkey(ii) for ii in range(len(new_monkeys))]

    for ii in range(len(monkeys)):
        monkey = monkeys[ii]
        new_monkey = new_monkeys[ii]
        monkey.items = [int(item) for item in new_monkey[1].lstrip("  Starting items: ").split(", ")]
        monkey.operation = eval(f"lambda old: {new_monkey[2].split(' = ')[1]}")
        monkey.test_val = int(new_monkey[3].split(" ")[-1])
        monkey.true_monkey = monkeys[int(new_monkey[4].split(" ")[-1])]
        monkey.false_monkey = monkeys[int(new_monkey[5].split(" ")[-1])]

    print("\n\n".join([str(monkey) for monkey in monkeys]))

    storage_modulus = 1
    for monkey in monkeys:
        storage_modulus *= monkey.test_val

    for ii in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspect_count += 1
                item = monkey.operation(item)
                item %= storage_modulus
                if item % monkey.test_val == 0:
                    monkey.true_monkey.items.append(item)
                else:
                    monkey.false_monkey.items.append(item)
            monkey.items.clear()

        if ii+1 == 1 or ii+1 == 20 or (ii+1) % 1000 == 0:
            print()
            print(f"== After round {ii+1} ==")
            print("\n".join([monkey.__repr__() for monkey in monkeys]))

    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    print(monkeys[0].inspect_count*monkeys[1].inspect_count)

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)
