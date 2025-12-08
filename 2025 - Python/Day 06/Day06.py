import operator
import time
from functools import reduce

def part1(input_lines):
    print(input_lines)
    input_lines = [line.split() for line in input_lines]

    problems = [*zip(*input_lines)]

    print(problems)

    total = 0
    for problem in problems:
        if problem[-1] == "*":
            total += reduce(operator.mul, [int(num) for num in problem[:-1]], 1)
        elif problem[-1] == "+":
            total += sum([int(num) for num in problem[:-1]])

    print(total)

def part2(input_lines):
    print(input_lines)

    input_lines = [list(line) for line in input_lines]

    numbers = [*zip(*input_lines)]

    total = 0
    problem_total = 0
    problem_operator = None
    for number in numbers:
        if all([x == " " for x in number]):
            continue

        if number[-1] == "*":
            total += problem_total
            problem_total = 1
            problem_operator = operator.mul
        elif number[-1] == "+":
            total += problem_total
            problem_total = 0
            problem_operator = operator.add
        number_int = int("".join(number[:-1]))
        problem_total = problem_operator(problem_total, number_int)

    total += problem_total
    print(total)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
