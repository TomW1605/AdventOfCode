import time

from readFile import readFile

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def part1(input_lines):
    grid = [list(line) for line in input_lines]
    result_grid = [['.']*len(grid[0]) for _ in range(len(grid))]
    count = 0
    for ii in range(len(grid)):
        for jj in range(len(grid[ii])):
            if grid[ii][jj] == 'X':
                for direction in directions:
                    if 0 <= ii + direction[0] < len(grid) and 0 <= jj + direction[1] < len(grid[ii]):
                        if grid[ii + direction[0]][jj + direction[1]] == 'M':
                            if 0 <= ii + 2 * direction[0] < len(grid) and 0 <= jj + 2 * direction[1] < len(grid[ii]):
                                if grid[ii + 2 * direction[0]][jj + 2 * direction[1]] == 'A':
                                    if 0 <= ii + 3 * direction[0] < len(grid) and 0 <= jj + 3 * direction[1] < len(grid[ii]):
                                        if grid[ii + 3 * direction[0]][jj + 3 * direction[1]] == 'S':
                                            print(f"found XMAS from ({ii}, {jj}) to ({ii + 3 * direction[0]}, {jj + 3 * direction[1]})")
                                            result_grid[ii][jj] = "X"
                                            result_grid[ii + direction[0]][jj + direction[1]] = "M"
                                            result_grid[ii + 2 * direction[0]][jj + 2 * direction[1]] = "A"
                                            result_grid[ii + 3 * direction[0]][jj + 3 * direction[1]] = "S"
                                            count += 1
    print("\n".join(["".join(line) for line in result_grid]))
    print(count)

def part2(input_lines):
    grid = [list(line) for line in input_lines]
    count = 0
    for ii in range(1, len(grid) - 1):
        for jj in range(1, len(grid[ii]) - 1):
            if grid[ii][jj] == 'A':
                if (
                        (
                                (grid[ii - 1][jj - 1] == 'M' and grid[ii + 1][jj + 1] == 'S') or
                                (grid[ii - 1][jj - 1] == 'S' and grid[ii + 1][jj + 1] == 'M')
                        ) and (
                                (grid[ii - 1][jj + 1] == 'M' and grid[ii + 1][jj - 1] == 'S') or
                                (grid[ii - 1][jj + 1] == 'S' and grid[ii + 1][jj - 1] == 'M')
                        )
                ):
                    count += 1
    print(count)

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
