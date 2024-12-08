import itertools
import operator
import time

def concat(in1, in2):
    return int(str(in1) + str(in2))

def part1(input_lines):
    equations = [{"result": int(result), "inputs": [int(i) for i in inputs.split(" ")]} for result, inputs in [line.split(": ") for line in input_lines]]

    total = 0
    for equation in equations:
        operators = list(itertools.product([operator.add, operator.mul], repeat=len(equation["inputs"]) - 1))
        for operator_set in operators:
            result = equation["inputs"][0]
            for ii in range(len(operator_set)):
                result = operator_set[ii](result, equation["inputs"][ii + 1])
            if result == equation["result"]:
                total += result
                break
        # print(operators)
    print(total)

def part2(input_lines):
    equations = [{"result": int(result), "inputs": [int(i) for i in inputs.split(" ")]} for result, inputs in [line.split(": ") for line in input_lines]]

    total = 0
    for equation in equations:
        operators = list(itertools.product([operator.add, operator.mul, concat], repeat=len(equation["inputs"]) - 1))
        for operator_set in operators:
            result = equation["inputs"][0]
            for ii in range(len(operator_set)):
                result = operator_set[ii](result, equation["inputs"][ii + 1])
            if result == equation["result"]:
                total += result
                break
        # print(operators)
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
