import re
import time

def expand_range(id_range):
    start, end = id_range.split('-')
    return list(range(int(start), int(end)+1))

def part1(input_lines):
    print(input_lines)

    ranges = input_lines.split(',')

    IDs = []
    for id_range in ranges:
        IDs += expand_range(id_range)
    print(IDs)

    total = 0
    for ID in IDs:
        ID = str(ID)
        if ID[:len(ID)//2] == ID[len(ID)//2:]:
            total += int(ID)

    print(total)

def part2(input_lines):
    print(input_lines)

    ranges = input_lines.split(',')

    IDs = []
    for id_range in ranges:
        IDs += expand_range(id_range)
    print(IDs)

    total = 0
    for ID in IDs:
        ID = str(ID)
        for ii in range(len(ID)//2):
            substr = ID[:ii+1]
            if ID.count(substr) * len(substr) == len(ID):
                total += int(ID)
                break

    print(total)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()[0]
    else:
        inputLines = open("input.txt", "r").read().splitlines()[0]

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
