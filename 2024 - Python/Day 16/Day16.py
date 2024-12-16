import math
import time
from enum import Enum

import cv2
import numpy as np

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
    value: float = 0
    dist: float = math.inf
    visited: bool = False
    # last: 'Position' = None
    last: list['Position']
    next: list['Position']
    penalty = 0
    type: str
    next_dist: float = math.inf

    def __init__(self, row_num, col_num, pos_type, visited):
        self.row = row_num
        self.col = col_num
        self.visited = visited
        self.type = pos_type
        self.last = []
        self.next = []

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

class Reindeer:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

def draw_grid(grid, scale_factor, wait = 0):
    image = np.zeros((len(grid), len(grid[0]), 3), dtype=np.uint8)
    for ii in range(len(grid)):
        for jj in range(len(grid[0])):
            if grid[ii][jj] == "O":
                image[ii][jj] = (19, 70, 140)
            elif grid[ii][jj] == "#":
                image[ii][jj] = (180, 180, 180)
            elif grid[ii][jj] == ".":
                image[ii][jj] = (0, 0, 0)
            elif grid[ii][jj] == "@":
                image[ii][jj] = (0, 0, 255)
    scaled_image = cv2.resize(image, (len(grid) * scale_factor, len(grid[0]) * scale_factor), interpolation=cv2.INTER_NEAREST)
    cv2.imshow(f"Warehouse", scaled_image)
    cv2.waitKey(wait)

def printGrid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None, scale_percent: int = 3000, wait: int = 1, highlight: Position = None):
    height = len(grid)
    width = len(grid[0])

    genPath = path
    if genPath is None and pos is not None:
        genPath = []
        last = pos.last[0] if 0 < len(pos.last) else None
        while last is not None:
            genPath.append(last)
            last = last.last[0] if 0 < len(last.last) else None

    imgArray = np.zeros((height, width, 3), dtype=np.uint8)
    for row in range(height):
        for col in range(width):
            imgArray[row][col] = (0, 0, 0)
            if grid[row][col].visited:
                imgArray[row][col] = (0, 0, 255)
            if grid[row][col] == pos or genPath is not None and grid[row][col] in genPath:
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

def Dijkstra(grid: list[list[Position]], direction: Direction, pos: Position, target: Position):
    loopNum = 0
    searchSpaces = [(pos, direction)]
    while not target.visited:
        pos_dir = min([space for space in searchSpaces if not space[0].visited])
        searchSpaces.remove(pos_dir)
        pos = pos_dir[0]
        direction = pos_dir[1]
        if loopNum % 1 == 0:
            printGrid(grid, pos=pos, wait=1)
        print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = []
        for search_direction in Directions:
            searchList.append([row+search_direction.y, col+search_direction.x, search_direction])
            if search_direction == direction:
                grid[row+search_direction.y][col+search_direction.x].penalty = 1
            else:
                grid[row+search_direction.y][col+search_direction.x].penalty = 1001

        adjacentSpaces = sorted([[grid[searchRow][searchCol], direction] for searchRow, searchCol, direction in searchList if not grid[searchRow][searchCol].visited])
        for space in adjacentSpaces:
            newDist = space[0].value + space[0].penalty + pos.dist
            if newDist <= math.inf: #space[0].dist:
                space[0].dist = newDist
                space[0].last.append(pos)
                # if newDist < pos.next_dist:
                #     pos.next = []
                pos.next.append(space[0])
                searchSpaces.append(space)

        pos.visited = True

def generate_paths(end: Position, grid: list[list[Position]]):
    printGrid(grid, highlight=end, wait=1)
    path_points = [end]
    next_points = end.last
    if len(next_points) > 0:
        min_dist = min([point.dist for point in next_points])
        for point in next_points:
            if point.dist == min_dist:
                path_points += generate_paths(point, grid)
                # print(len(path_points))
    return path_points

def part1(input_lines):
    grid = []
    start = None
    end = None
    for row_num, row in enumerate(input_lines):
        grid.append([])
        for col_num, char in enumerate(row):
            pos = Position(row_num, col_num, char, False)
            if char == "#":
                pos.value = math.inf
            elif char == "S":
                pos.value = 0
                pos.dist = 0
                start = pos
            elif char == "E":
                pos.value = 0
                end = pos
            else:
                pos.value = 0
            grid[row_num].append(pos)
    # reindeer = Reindeer(start, Direction.RIGHT)
    Dijkstra(grid, Direction.RIGHT, start, end)
    print(end.dist)
    # printGrid(grid, pos=end, wait=0)

def part2(input_lines):
    grid = []
    start = None
    end = None
    for row_num, row in enumerate(input_lines):
        grid.append([])
        for col_num, char in enumerate(row):
            pos = Position(row_num, col_num, char, False)
            if char == "#":
                pos.value = math.inf
            elif char == "S":
                pos.value = 0
                pos.dist = 0
                start = pos
            elif char == "E":
                pos.value = 0
                end = pos
            else:
                pos.value = 0
            grid[row_num].append(pos)
    # reindeer = Reindeer(start, Direction.RIGHT)
    Dijkstra(grid, Direction.RIGHT, start, end)
    paths = generate_paths(end, grid)
    print(len(paths))
    printGrid(grid, path=paths, pos=end, wait=0)

if __name__ == '__main__':
    test = 1
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
