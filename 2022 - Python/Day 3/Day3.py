from readFile import readFile

def part1(input_lines):
    print(input_lines)

    priority = 0

    for rucksack in input_lines:
        first_comp = set(rucksack[:len(rucksack)//2])
        second_comp = set(rucksack[len(rucksack)//2:])

        for char in first_comp:
            if char in second_comp:
                if char.islower():
                    priority += ord(char)-96
                else:
                    priority += ord(char)-64+26

    print(priority)


def part2(input_lines):
    print(input_lines)

    priority = 0

    for ii in range(0, len(input_lines), 3):
        group = [set(input_lines[ii]), set(input_lines[ii+1]), set(input_lines[ii+2])]

        for char in group[0]:
            if char in group[1] and char in group[2]:
                if char.islower():
                    priority += ord(char)-96
                else:
                    priority += ord(char)-64+26

    print(priority)



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

