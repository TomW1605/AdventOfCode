import itertools
import time

def calc_area(point1, point2):
    return (abs(point1[0] - point2[0])+1) * (abs(point1[1] - point2[1])+1)

def part1(input_lines):
    print(input_lines)

    red_tiles = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in input_lines]
    print(red_tiles)

    max_area = 0
    for point1, point2 in itertools.combinations(red_tiles, 2):
        print(point1, point2, calc_area(point1, point2))
        max_area = max(max_area, calc_area(point1, point2))

    print(max_area)

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 0
    part = 1

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
