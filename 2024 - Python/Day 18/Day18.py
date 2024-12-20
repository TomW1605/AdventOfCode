import math
import time
from enum import Enum

import cv2
import numpy as np
import tqdm

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return True

    @property
    def x(self):
        return self.value[1]

    @property
    def y(self):
        return self.value[0]
Directions = Direction

class Position:
    row: int
    col: int
    value: float = 1
    _start_dist: float = math.inf
    visited: bool = False
    last: 'Position' = None
    type: str

    def __init__(self, row_num, col_num, pos_type, visited):
        self.row = row_num
        self.col = col_num
        self.visited = visited
        self.type = pos_type
        self.path = []
        self.dist = self._start_dist

    def reset(self):
        self.visited = False
        self.last = None
        self.path = []
        self.dist = self._start_dist

    def _is_valid_operand(self, other):
        return hasattr(other, "row") and hasattr(other, "col") and hasattr(other, "value") and hasattr(other, "dist")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.col == other.col and self.row == other.row

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.dist < other.dist

    def __str__(self):
        return f"({self.row}, {self.col}): ({self.value}, {self.dist}, {self.visited})"

    def __int__(self):
        return int(self.value) if self.value < math.inf else 0

    def __float__(self):
        return float(self.value)

def printGrid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None, scale_percent: int = 3000, wait: int = 1, highlight: Position = None):
    height = len(grid)
    width = len(grid[0])

    if pos is not None and path is None:
        if pos.path is not None:
            path = pos.path
        else:
            path = []
            last = pos.last
            while last is not None:
                path.append(last)
                last = last.last

    imgArray = np.zeros((height, width, 3), dtype=np.uint8)
    for row in range(height):
        for col in range(width):
            imgArray[row][col] = (0, 0, 0)
            if grid[row][col].visited:
                imgArray[row][col] = (0, 0, 255)
            if grid[row][col] == pos or path is not None and grid[row][col] in path:
                imgArray[row][col] = (255, 0, 0)

            if grid[row][col].type == "#":
                imgArray[row][col] = (180, 180, 180)
            if grid[row][col].type in ["S", "E"]:
                imgArray[row][col] = (0, 255, 0)

            if highlight is not None and grid[row][col] == highlight:
                imgArray[row][col] = (0, 255, 255)

    imgWidth = int((height)*scale_percent/100)
    imgHeight = int((width)*scale_percent/100)
    # cv2.imwrite(f"./images/{printGrid.imageNum}.jpg", cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    # printGrid.imageNum += 1
    cv2.imshow('image', cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(wait)

def Dijkstra(grid: list[list[Position]], pos: Position, target: Position, print_grid: bool = False, print_freq: int = 1):
    loopNum = 0
    searchSpaces = [pos]
    while not target.visited:
        if len(searchSpaces) <= 0:
            return False
        pos = min([space for space in searchSpaces if not space.visited])
        searchSpaces.remove(pos)
        if loopNum % print_freq == 0 and print_grid:
            printGrid(grid, pos=pos, wait=1, scale_percent=1000)
        # print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = []
        for search_direction in Directions:
            if 0 <= row+search_direction.y < len(grid) and 0 <= col+search_direction.x < len(grid[0]):
                searchList.append((row+search_direction.y, col+search_direction.x))

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited])
        for space in adjacentSpaces:
            newDist = space.value + pos.dist
            if newDist < space.dist:
                space.dist = newDist
                space.last = pos
                space.path = pos.path + [pos]
                searchSpaces.append(space)

        pos.visited = True
    return True

def part1(input_lines, grid_size, num_bytes):
    grid = [[Position(y, x, ".", False) for x in range(grid_size)] for y in range(grid_size)]
    for line in input_lines[:num_bytes]:
        x, y = map(int, line.split(","))
        grid[y][x].type = "#"
        grid[y][x].value = math.inf
    # print('\n'.join([''.join([cell.type for cell in row]) for row in grid]))
    start = grid[0][0]
    start.dist = 0
    start.type = "S"
    end = grid[grid_size-1][grid_size-1]
    end.type = "E"
    Dijkstra(grid, start, end, print_grid=True, print_freq=10)
    print(end.dist)
    printGrid(grid, pos=end, wait=0, scale_percent=1000)

def part2(input_lines, grid_size):
    grid = [[Position(y, x, ".", False) for x in range(grid_size)] for y in range(grid_size)]
    start = grid[0][0]
    start._start_dist = 0
    start.dist = 0
    start.type = "S"
    end = grid[grid_size-1][grid_size-1]
    end.type = "E"
    Dijkstra(grid, start, end)
    # for line in input_lines:
    for ii in (t := tqdm.tqdm(range(len(input_lines)), unit="line", postfix={"shortest path": 0})):
        line = input_lines[ii]
        x, y = map(int, line.split(","))
        grid[y][x].type = "#"
        grid[y][x].value = math.inf
        if grid[y][x] in end.path:
            for row in grid:
                for cell in row:
                    cell.reset()
            if not Dijkstra(grid, start, end):
                print(line)
                break
        t.set_postfix({"shortest path": end.dist})
    printGrid(grid, pos=end, wait=0, scale_percent=1000)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
        grid_size = 7
        num_bytes = 12
    else:
        inputLines = open("input.txt", "r").read().splitlines()
        grid_size = 71
        num_bytes = 1024

    if part == 1:
        part1(inputLines, grid_size, num_bytes)
    elif part == 2:
        part2(inputLines, grid_size)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
