from readFile import readFile


def part1(input_lines):
    print(input_lines)
    total = 0
    for pair in input_lines:
        elf1, elf2 = pair.split(",")

        elf1 = elf1.split("-")
        elf2 = elf2.split("-")

        elf1 = range(int(elf1[0]), int(elf1[1])+1)
        elf2 = range(int(elf2[0]), int(elf2[1])+1)

        if all(x in elf1 for x in elf2) or all(x in elf2 for x in elf1):
            total += 1

    print(total)




def part2(input_lines):
    print(input_lines)
    total = 0
    for pair in input_lines:
        elf1, elf2 = pair.split(",")

        elf1 = elf1.split("-")
        elf2 = elf2.split("-")

        elf1 = range(int(elf1[0]), int(elf1[1])+1)
        elf2 = range(int(elf2[0]), int(elf2[1])+1)

        if any(x in elf1 for x in elf2) or any(x in elf2 for x in elf1):
            total += 1

    print(total)


if __name__ == "__main__":
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

