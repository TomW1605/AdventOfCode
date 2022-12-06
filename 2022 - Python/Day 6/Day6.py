from readFile import readFile


def part1(input_lines):
    print(input_lines)

    for ii in range(4, len(input_lines)):
        if len(set(input_lines[ii-4:ii])) == 4:
            break
    print(ii)

def part2(input_lines):
    print(input_lines)

    for ii in range(14, len(input_lines)):
        if len(set(input_lines[ii-14:ii])) == 14:
            break
    print(ii)


if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")[0]
    else:
        inputLines = readFile("input.txt")[0]

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

