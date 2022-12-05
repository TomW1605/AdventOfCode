import re


def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x)
    return output


class Crate:
    crate_below = None
    crates_above = 0
    creat_ID = ''

    def __init__(self, ID):
        self.creat_ID = ID


class Stack:
    top_crate = None
    stack_height = 0

    def add_creat(self, creat: Crate):
        if self.top_crate:
            creat.crate_below = self.top_crate

        self.top_crate = creat
        self.stack_height += 1


class Move:
    number = 0
    start = 0
    end = 0


def part1(input_lines):
    print(input_lines)
    stack_input = []
    move_input = []
    processing_stacks = True
    for line in input_lines:
        line = line.strip("\n")
        if line == "":
            processing_stacks = False
            continue

        if processing_stacks:
            stack_input.append(line)
        else:
            move_input.append(line)

    print(move_input)

    stacks = []
    stack_input = stack_input[:-1]
    stack_input.reverse()
    for row in stack_input:
        crates_on_row = re.findall('[ \\[]( |.)[ \\]] ?', row)

        for ii in range(0, len(crates_on_row)):
            if len(stacks) <= ii:
                stacks.append(Stack())

            if crates_on_row[ii] != " ":
                crate = Crate(crates_on_row[ii])
                stacks[ii].add_creat(crate)


    moves = []


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

