import time

from readFile import readFile


def find_mirror(pattern, horizontal=False, old_mirror_line=-1):
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
            if horizontal:
                new_mirror_line = ii * 100
            else:
                new_mirror_line = ii
            if new_mirror_line != old_mirror_line:
                return new_mirror_line

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
    horizontal_total = 0
    total = 0

    for pattern in patterns:
        old_mirror_line = max(
            find_mirror(pattern, False),
            find_mirror([''.join(x) for x in zip(*pattern)], True)
        )
        for ii in range(len(pattern)):
            mirror_found = False
            for jj in range(len(pattern[ii])):
                new_pattern = pattern[:]
                if pattern[ii][jj] == '.':
                    line = list(pattern[ii])
                    line[jj] = '#'
                    new_pattern[ii] = ''.join(line)
                else:
                    line = list(pattern[ii])
                    line[jj] = '.'
                    new_pattern[ii] = ''.join(line)
                mirror_line = max(
                    find_mirror(new_pattern, False, old_mirror_line),
                    find_mirror([''.join(x) for x in zip(*new_pattern)], True, old_mirror_line)
                )
                if mirror_line > 0:
                    print(mirror_line)
                    total += mirror_line
                    mirror_found = True
                    break

                # mirror_line = find_mirror(new_pattern, old_mirror_line)
                # if mirror_line > 0 and mirror_line != old_mirror_line:
                #     print(mirror_line)
                #     vertical_total += mirror_line
                #     mirror_found = True
                #     break
                # mirror_line = find_mirror([''.join(x) for x in zip(*new_pattern)], old_mirror_line)
                # if mirror_line > 0 and mirror_line*100 != old_mirror_line:
                #     print(mirror_line * 100)
                #     horizontal_total += mirror_line
                #     mirror_found = True
                #     break
            if mirror_found:
                break

    # print(vertical_total)
    # print(horizontal_total)
    # print(vertical_total + (horizontal_total * 100))
    print(total)

#26439

if __name__ == '__main__':
    test = 0
    part = 2

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