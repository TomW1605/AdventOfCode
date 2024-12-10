import time
from enum import Enum

class Directions(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

def step_pt1(grid, x, y, ends: set):
    if grid[y][x] == 9:
        ends.add((x, y))
        return ends
    for direction in Directions:
        if 0 <= x + direction.value[0] < len(grid[0]) and 0 <= y + direction.value[1] < len(grid):
            if grid[y + direction.value[1]][x + direction.value[0]] == grid[y][x] + 1:
                ends = step_pt1(grid, x + direction.value[0], y + direction.value[1], ends)
    return ends

def part1(input_lines):
    grid = [[int(point) for point in line] for line in input_lines]
    total = 0
    for ii in range(len(grid)):
        for jj in range(len(grid[ii])):
            if grid[ii][jj] == 0:
                # print(len(step_pt1(grid, jj, ii, set())))
                total += len(step_pt1(grid, jj, ii, set()))
    print(total)

def step_pt2(grid, x, y, ends: list):
    if grid[y][x] == 9:
        ends.append((x, y))
        return ends
    for direction in Directions:
        if 0 <= x + direction.value[0] < len(grid[0]) and 0 <= y + direction.value[1] < len(grid):
            if grid[y + direction.value[1]][x + direction.value[0]] == grid[y][x] + 1:
                ends = step_pt2(grid, x + direction.value[0], y + direction.value[1], ends)
    return ends

def part2(input_lines):
    grid = [[int(point) for point in line] for line in input_lines]
    total = 0
    for ii in range(len(grid)):
        for jj in range(len(grid[ii])):
            if grid[ii][jj] == 0:
                # print(len(step_pt2(grid, jj, ii, list())))
                total += len(step_pt2(grid, jj, ii, list()))
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
