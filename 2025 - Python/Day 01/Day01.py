import time

class Dial:
    min = 0
    max = 99
    value = 50

    def left(self, steps):
        old_value = self.value
        new_value = self.value - steps
        if new_value < self.min:
            self.value = self.max + new_value + 1
            return 1 if old_value != 0 else 0
        else:
            self.value = new_value
            return 0


    def right(self, steps):
        new_value = self.value + steps
        if new_value > self.max:
            self.value = self.min + new_value - self.max - 1
            return 1 if self.value != 0 else 0
        else:
            self.value = new_value
            return 0

def part1(input_lines):
    print(input_lines)

    zero_count = 0
    dial = Dial()
    for line in input_lines:
        direction = line[0]
        steps = int(line[1:]) % 100
        if direction == "L":
            dial.left(steps)
        elif direction == "R":
            dial.right(steps)
        print(dial.value)
        if dial.value == 0:
            zero_count += 1

    print(zero_count)

def part2(input_lines):
    print(input_lines)

    zero_count = 0
    dial = Dial()
    print(f"{dial.value} {zero_count}")
    for line in input_lines:
        direction = line[0]
        steps = int(line[1:])
        zero_count += steps // 100
        if direction == "L":
            zero_count += dial.left(steps % 100)
        elif direction == "R":
            zero_count += dial.right(steps % 100)
        if dial.value == 0:
            zero_count += 1
        print(f"{line} {dial.value} {zero_count}")

    if dial.value == 0:
        zero_count += 1
    print(zero_count)

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
