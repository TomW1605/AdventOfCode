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
    crate_ID = ''

    def __init__(self, ID):
        self.crate_ID = ID

    def __str__(self):
        return self.crate_ID

    def __repr__(self):
        return self.__str__()


class Stack:
    top_crate = None

    def __str__(self):
        if not self.top_crate:
            return

        crate = self.top_crate
        stack_str = ""
        while crate is not None:
            stack_str += f"[{crate.crate_ID}]\n"
            crate = crate.crate_below

        return stack_str

    def __repr__(self):
        return "\n" + self.__str__()

    def add_crate(self, crate: Crate):
        if self.top_crate:
            crate.crate_below = self.top_crate

        self.top_crate = crate

    def remove_crate(self, crate: Crate):
        self.top_crate = crate.crate_below


class Move:
    number = 0
    start = 0
    end = 0

    def __init__(self, values):
        self.number = values[0]
        self.start = values[1]
        self.end = values[2]

    def __str__(self):
        return f"move {self.number} from {self.start} to {self.end}"

    def __repr__(self):
        return self.__str__()


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
                stacks[ii].add_crate(crate)

    moves = []
    for row in move_input:
        parsed_row = re.findall("move (\\d+?) from (\\d+?) to (\\d+?)", row)
        moves.append(Move(parsed_row[0]))

    for move in moves:


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

