from readFile import readFile
from dataclasses import dataclass

@dataclass
class Instruction:
    operation: str
    argument: int
    run: bool = False

    def reset(self):
        self.run = False
        return self

def runInstruction(program: list[Instruction], index: int, accumulator: int) -> (int, bool):
    if index == len(program):
        return accumulator, True
    elif program[index].run:
        return accumulator, False

    program[index].run = True
    match program[index].operation:
        case 'acc':
            return runInstruction(program, index+1, accumulator+program[index].argument)
        case 'jmp':
            return runInstruction(program, index+program[index].argument, accumulator)
        case _:
            return runInstruction(program, index+1, accumulator)

def part1(input_lines):
    print(input_lines)
    program = [Instruction(line.split(" ")[0], int(line.split(" ")[1])) for line in input_lines]

    print(runInstruction(program, 0, 0))

def part2(input_lines):
    print(input_lines)
    program = [Instruction(line.split(" ")[0], int(line.split(" ")[1])) for line in input_lines]

    for line in program:
        if line.operation == "acc":
            continue

        match line.operation:
            case 'nop':
                line.operation = "jmp"
            case 'jmp':
                line.operation = "nop"
        print(program)
        accumulator, terminated = runInstruction(program.copy(), 0, 0)
        if terminated:
            print(accumulator)
            break
        else:
            program = [line.reset() for line in program]
            match line.operation:
                case 'nop':
                    line.operation = "jmp"
                case 'jmp':
                    line.operation = "nop"

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

