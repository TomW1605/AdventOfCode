import re
import time

from readFile import readFile

def parse_input(input_lines):
    input_program = "".join(input_lines)
    program = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input_program)
    program = [i.replace("'", "") for i in program]
    return program

enable = True

def mul(a, b):
    if enable:
        return a * b
    else:
        return 0

def do():
    global enable
    enable = True
    return 0

def dont():
    global enable
    enable = False
    return 0

def part1(input_lines):
    program = parse_input(input_lines)
    total = sum(eval(i) for i in program if "mul" in i)
    print(total)

def part2(input_lines):
    program = parse_input(input_lines)
    total = sum(eval(i) for i in program)
    print(total)

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
