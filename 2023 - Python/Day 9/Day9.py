import time

from readFile import readFile


def part1(input_lines):
    print(input_lines)

    total = 0

    for history in input_lines:
        history = [int(x) for x in history.split(' ')]
        sequence = [history]
        while not all(x == 0 for x in sequence[-1]):
            next_step = []
            for ii in range(len(sequence[-1])-1):
                next_step.append(sequence[-1][ii+1]-sequence[-1][ii])
            sequence.append(next_step)

        print('\n'.join([str(x) for x in sequence]))

        for ii in range(len(sequence)-2, -1, -1):
            sequence[ii].append(sequence[ii][-1]+sequence[ii+1][-1])

        print('\n'.join([str(x) for x in sequence]))
        print()

        total += sequence[0][-1]

    print(total)


def part2(input_lines):
    print(input_lines)

    total = 0

    for history in input_lines:
        history = [int(x) for x in history.split(' ')]
        sequence = [history]
        while not all(x == 0 for x in sequence[-1]):
            next_step = []
            for ii in range(len(sequence[-1])-1):
                next_step.append(sequence[-1][ii+1]-sequence[-1][ii])
            sequence.append(next_step)

        print('\n'.join([str(x) for x in sequence]))

        for ii in range(len(sequence)-2, -1, -1):
            sequence[ii][0] = sequence[ii][0]-sequence[ii+1][0]

        print('\n'.join([str(x) for x in sequence]))
        print()

        total += sequence[0][0]

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