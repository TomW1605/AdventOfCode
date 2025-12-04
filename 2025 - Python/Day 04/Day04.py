import time

directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],          [0, 1],
    [1, -1], [1, 0], [1, 1]
]


def part1(input_lines):
    print(input_lines)

    total = 0
    for ii in range(len(input_lines)):
        for jj in range(len(input_lines[ii])):
            if input_lines[ii][jj] == ".":
                continue
            neighbours = 0
            for direction in directions:
                new_x = ii + direction[0]
                new_y = jj + direction[1]
                if 0 <= new_x < len(input_lines) and 0 <= new_y < len(input_lines[ii]):
                    if input_lines[new_x][new_y] == "@":
                        neighbours += 1
            if neighbours < 4:
                total += 1
    print(total)

def part2(input_lines):
    print(input_lines)
    input_lines = [list(line) for line in input_lines]

    removed = [0]
    count = 0
    while removed != []:
        removed = []
        for ii in range(len(input_lines)):
            for jj in range(len(input_lines[ii])):
                if input_lines[ii][jj] == ".":
                    continue
                neighbours = 0
                for direction in directions:
                    new_x = ii + direction[0]
                    new_y = jj + direction[1]
                    if 0 <= new_x < len(input_lines) and 0 <= new_y < len(input_lines[ii]):
                        if input_lines[new_x][new_y] == "@":
                            neighbours += 1
                if neighbours < 4:
                    removed.append((ii, jj))

        count += len(removed)
        for ii, jj in removed:
            input_lines[ii][jj] = "."

    print(count)

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
