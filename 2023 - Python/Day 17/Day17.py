import math
import time

import cv2
import numpy as np
from termcolor import colored

from readFile import readFile

class Position:
    row: int
    col: int
    value: float = 0
    dist: float = math.inf
    visited: bool = False
    last: 'Position' = None
    penalty = 0
    consecutive_straight_moves: int = 0

    def __init__(self, rowNum, colNum, value, visited):
        self.row = rowNum
        self.col = colNum
        self.value = value
        self.visited = visited

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
        return f"({self.row}, {self.col}): ({self.value}, {self.visited})"

    def __int__(self):
        return int(self.value) if self.value < math.inf else 0

    def __float__(self):
        return float(self.value)

def printGrid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None, scale_percent: int = 3000, showOnly: bool = True, padWidth: int = 1, wait: int = 1):
    height = len(grid)
    width = len(grid[0])

    genPath = None
    if path is None and pos is not None:
        genPath = []
        last = pos.last
        while last is not None:
            genPath.append(last)
            last = last.last

    imgArray = np.zeros([height-padWidth*2, width-padWidth*2, 3])
    for row in range(padWidth, height-padWidth):
        for col in range(padWidth, width-padWidth):
            colour = 'green'
            pixColour = [0, 1, 0]
            if path is not None and grid[row][col] in path or grid[row][col].visited:
                colour = 'red'
                pixColour = [0, 0, 1]
            if grid[row][col] == pos or genPath is not None and grid[row][col] in genPath:
                colour = 'blue'
                pixColour = [1, 0, 0]
            imgArray[row-1][col-1] = pixColour
            if not showOnly:
                print(colored(str(grid[row][col].value), colour), end='')
        if not showOnly:
            print("")
    if not showOnly:
        print("")

    imgWidth = int((height-2)*scale_percent/100)
    imgHeight = int((width-2)*scale_percent/100)
    cv2.imwrite(f"./images/{printGrid.imageNum}.jpg", 255*cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    printGrid.imageNum += 1
    cv2.imshow('image', 255*cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(wait)

printGrid.imageNum = 1

def Dijkstra(grid: list[list[Position]], pos: Position, target: Position):
    loopNum = 0
    searchSpaces = [pos]
    # consecutive_straight_moves = 0  # Counter for consecutive straight moves
    max_consecutive_straight_moves = 3  # Maximum allowed consecutive straight moves
    while not target.visited:
        pos = min([space for space in searchSpaces if not space.visited])
        searchSpaces.remove(pos)
        printGrid(grid, pos=pos, wait=1)
        # print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]

        last_straight_line = 0
        temp_last = pos.last
        while temp_last and temp_last.row == pos.row:
            last_straight_line += 1
            temp_last = temp_last.last
        while temp_last and temp_last.col == pos.col:
            last_straight_line += 1
            temp_last = temp_last.last

        if last_straight_line == 3:
            if pos.last.row == pos.row:
                searchList.pop(2)
                searchList.pop(1)
            elif pos.last.col == pos.col:
                searchList.pop(3)
                searchList.pop(0)

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited])
        for space in adjacentSpaces:
            newDist = space.value+pos.dist
            if newDist < space.dist:
                space.dist = newDist
                space.last = pos
                searchSpaces.append(space)

        pos.visited = True

def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    intGrid = [[math.inf]*(width+2)]+[[math.inf]+[int(point) for point in list(line)]+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]
    grid = []
    for rowNum in range(len(intGrid)):
        row = []
        for colNum in range(len(intGrid[0])):
            row.append(Position(rowNum, colNum, intGrid[rowNum][colNum], visited=True if intGrid[rowNum][colNum] == math.inf else False))
        grid.append(row)
    #print(grid)
    printGrid(grid)

    pos = grid[1][1]
    pos.dist = 0
    target = grid[height][width]
    #findPathBFS(grid, pos, target, [], -pos.value, math.inf)
    Dijkstra(grid, pos, target)
    print(target.dist)
    printGrid(grid, pos=target, wait=0)


def part2(input_lines):
    print(input_lines)


if __name__ == '__main__':
    test = 1
    part = 1

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