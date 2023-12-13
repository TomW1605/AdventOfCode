import time

from readFile import readFile


def find_mirror(pattern):
    width = len(pattern[0])
    for ii in range(1, width):
        reflection = True
        for row in pattern:
            if ii < width / 2:
                left = row[:ii]
                right = row[ii:ii + ii]
            else:
                left = row[ii - (width - ii):ii]
                right = row[ii:]

            # print(f'{left} : {right}')

            reflection = left == right[::-1]

            if not reflection:
                break

        if reflection:
            return ii

    return 0

def part1(input_lines):
    # print(input_lines)

    patterns = []
    new_pattern = []
    for line in input_lines:
        if line == '':
            patterns.append(new_pattern)
            new_pattern = []
            continue
        new_pattern.append(line)
    patterns.append(new_pattern)

    # print(patterns)

    vertical_total = 0

    for xx in range(len(patterns)):
        mirror_line = find_mirror(patterns[xx])
        if mirror_line > 0:
            vertical_total += mirror_line
            patterns[xx] = None

    print(vertical_total)

    patterns = [[''.join(x) for x in zip(*pattern)] for pattern in patterns if pattern is not None]
    # print(patterns)

    horizontal_total = 0

    for xx in range(len(patterns)):
        mirror_line = find_mirror(patterns[xx])
        if mirror_line > 0:
            horizontal_total += mirror_line

    print(horizontal_total)

    print(vertical_total + (horizontal_total * 100))

def part2(input_lines):
    print(input_lines)


if __name__ == '__main__':
    test = 0
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

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")