import re

from readFile import readFile


def part1(input_lines):
    print(input_lines)

    times = [int(x) for x in re.split(' +', input_lines[0])[1:]]
    dists = [int(x) for x in re.split(' +', input_lines[1])[1:]]
    races = [(times[ii], dists[ii]) for ii in range(len(times))]

    print(races)

    total = 1

    for time, dist in races:
        win_options = 0
        # print(time)
        # print(dist)
        for held in range(time):
            if (time-held)*held > dist:
                win_options += 1
        total *= win_options

    print(total)

def part2(input_lines):
    print(input_lines)

    time = int(input_lines[0].replace(' ', '').split(':')[1])
    dist = int(input_lines[1].replace(' ', '').split(':')[1])

    print(time)
    print(dist)

    win_options = 0
    for held in range(time):
        if (time - held) * held > dist:
            win_options += 1

    print(win_options)


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

