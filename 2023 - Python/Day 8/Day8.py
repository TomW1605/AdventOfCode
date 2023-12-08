import math
import time

from readFile import readFile


def part1(directions, path):
    print(directions)
    print(path)

    current_node = 'AAA'
    print(current_node)
    ii = 0
    steps = 0
    while current_node != 'ZZZ':
        if directions[ii] == 'L':
            current_node = path[current_node][0]
        elif directions[ii] == 'R':
            current_node = path[current_node][1]
        print(current_node)
        steps += 1

        ii += 1
        if ii == len(directions):
            ii = 0

    print(steps)

def part2(directions, path):
    print(directions)
    print(path)

    start_nodes = [node for node in path.keys() if node[-1] == 'A']
    print(start_nodes)
    ii = 0
    steps = []
    for jj in range(len(start_nodes)):
        current_node = start_nodes[jj]
        current_path_steps = 0

        while current_node[-1] != 'Z':
            if directions[ii] == 'L':
                current_node = path[current_node][0]
            elif directions[ii] == 'R':
                current_node = path[current_node][1]
            print(current_node)
            current_path_steps += 1

            ii += 1
            if ii == len(directions):
                ii = 0

        steps.append(current_path_steps)
    print(math.lcm(*steps))

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    directions = inputLines.pop(0)
    inputLines.pop(0)

    path = {line[0:3]: (line[7:10], line[12:15]) for line in inputLines}

    if part == 1:
        part1(directions, path)
    elif part == 2:
        part2(directions, path)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")