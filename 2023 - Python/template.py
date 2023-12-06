import time

from readFile import readFile


def part1(input_lines):
    print(input_lines)


def part2(input_lines):
    print(input_lines)


if __name__ == '__main__':
    test = 1
    part = 1

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{seconds:06.3f}")