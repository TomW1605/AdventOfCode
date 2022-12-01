from readFile import readFile

def part1(input_lines):
    print(input_lines)

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 1
    part = 1

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

