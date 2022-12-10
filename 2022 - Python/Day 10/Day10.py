from readFile import readFile


def part1(input_lines):
    print(input_lines)

    instructions = []
    for line in input_lines:
        if line.startswith("noop"):
            instructions.append(line)
        elif line.startswith("addx"):
            instructions.append("noop")
            instructions.append(line)

    x = 1
    cycle = 1
    total = 0
    for instruction in instructions:
        if cycle in [20, 60, 100, 140, 180, 220]:
            print(cycle, x)
            signal = x*cycle
            print(signal)
            total += signal

        cycle += 1

        if instruction.startswith("addx"):
            x += int(instruction.split()[1])

        """if cycle in [20, 60, 100, 140, 180, 220]:
            print(cycle, x)
            signal = x * cycle
            print(signal)
            total += signal"""

    print(total)

def part2(input_lines):
    print(input_lines)

    instructions = []
    for line in input_lines:
        if line.startswith("noop"):
            instructions.append(line)
        elif line.startswith("addx"):
            instructions.append("noop")
            instructions.append(line)

    x = 1
    cycle = 1
    crt_pos = 0
    for instruction in instructions:
        if crt_pos in [x-1, x, x+1]:
            print("#", end="")
        else:
            print(" ", end="")

        cycle += 1
        crt_pos += 1
        if crt_pos == 40:
            crt_pos = 0
            print()

        if instruction.startswith("addx"):
            x += int(instruction.split()[1])


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

