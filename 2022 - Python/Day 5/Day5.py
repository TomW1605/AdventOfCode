import re


def readFile(file):
    output = []
    f = open(file, "r")
    output = f.read()
    """for x in f:
        output.append(x)"""
    return output


class Crate:
    crate_below = None
    crate_above = None
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
            return ""

        crate = self.top_crate
        stack_str = ""
        while crate is not None:
            stack_str += f"[{crate.crate_ID}]\n"
            crate = crate.crate_below

        return stack_str

    def __repr__(self):
        return "\n" + self.__str__()

    def add_crate(self, crate: Crate):
        crate.crate_below = self.top_crate

        if self.top_crate:
            self.top_crate.crate_above = crate

        new_top = crate
        while new_top.crate_above is not None:
            new_top = new_top.crate_above
        self.top_crate = new_top

    def remove_crate(self, crate: Crate):
        self.top_crate = crate.crate_below
        if self.top_crate:
            self.top_crate.crate_above = None

    def select_crate(self, num):
        ii = 1
        crate = self.top_crate
        while ii < num and crate is not None:
            crate = crate.crate_below
            ii += 1

        return crate


class Move:
    number = 0
    start = 0
    end = 0

    def __init__(self, values):
        self.number = int(values[0])
        self.start = int(values[1])-1
        self.end = int(values[2])-1

    def __str__(self):
        return f"move {self.number} from {self.start} to {self.end}"

    def __repr__(self):
        return self.__str__()


def make_stacks(input_lines):
    stack_input = []
    for line in input_lines.split('\n'):
        if line == "":
            break

        stack_input.append(line)

    stacks = []
    stack_input = stack_input[:-1]
    stack_input.reverse()
    for row in stack_input:
        crates_on_row = re.findall(r'[ \[]( |.)[ \]] ?', row)

        for ii in range(0, len(crates_on_row)):
            if len(stacks) <= ii:
                stacks.append(Stack())

            if crates_on_row[ii] != " ":
                crate = Crate(crates_on_row[ii])
                stacks[ii].add_crate(crate)

    return stacks


def part1(input_lines):
    print(input_lines)

    stacks = make_stacks(input_lines)

    #print(stacks)

    moves = re.findall(r"move (\d+?) from (\d+?) to (\d+?)", input_lines)
    for move in moves:
        move = Move(move)

        ii = 0
        while ii < move.number:
            crate = stacks[move.start].top_crate
            stacks[move.start].remove_crate(crate)
            stacks[move.end].add_crate(crate)
            ii += 1

    #print(stacks)
    for stack in stacks:
        print(stack.top_crate, end="")


def part2(input_lines):
    print(input_lines)

    stacks = make_stacks(input_lines)

    #print(stacks)

    moves = re.findall(r"move (\d+?) from (\d+?) to (\d+?)", input_lines)
    for move in moves:
        move = Move(move)

        crate = stacks[move.start].select_crate(move.number)
        stacks[move.start].remove_crate(crate)
        stacks[move.end].add_crate(crate)

    #print(stacks)
    for stack in stacks:
        print(stack.top_crate, end="")


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

