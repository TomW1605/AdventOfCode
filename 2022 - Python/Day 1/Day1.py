import sys

print(sys.path)

from readFile import readFile


def part1(input_lines):
    print(input_lines)
    largest = 0
    current = 0
    for food in input_lines:
        if food == "":
            if current > largest:
                largest = current
            current = 0
        else:
            current += int(food)
    print(largest)


def part2(input_lines):
    print(input_lines)
    elves = []
    current = 0
    for food in input_lines:
        if food == "":
            elves.append(current)
            current = 0
        else:
            current += int(food)
    elves.sort(reverse=True)
    print(elves)
    print(sum(elves[:3]))

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

