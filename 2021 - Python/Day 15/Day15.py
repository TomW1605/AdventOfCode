import math
import os
import timeit
from dataclasses import dataclass

from matplotlib import pyplot as plt
from termcolor import colored
from PIL import Image
import numpy as np
import cv2


#from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

class Position:
    pass

@dataclass
class Position:
    row: int
    col: int
    value: float = 0
    dist: float = math.inf
    visited: bool = False
    last: Position = None

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

def printGrid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None, scale_percent: int = 1000, showOnly: bool = True, padWidth: int = 1):
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
    cv2.waitKey(1)
printGrid.imageNum = 1

def findPath(grid: list[list[Position]], pos: Position, target: Position, path: list[Position], risk: float, bestPath: float):
    print(pos)
    #printGrid(grid, pos)
    printGrid(grid, path, pos)
    row = pos.row
    col = pos.col

    path.append(pos)
    risk += pos.value
    #pos.visited = True
    #print(pos)
    #print(grid)
    #grid[row][col] = pos

    if pos == target:
        #if toPrint:
        #print("\n".join([str(cord) for cord in path]))
        print(risk)
        printGrid(grid, path)
        #paths.append(tuple(path))
        bestPath = risk
    elif risk < bestPath:
        searchList = [
                            [row - 1, col],
            [row, col - 1],                 [row, col + 1],
                            [row + 1, col]
        ]

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if grid[searchRow][searchCol] not in path and grid[searchRow][searchCol].value < math.inf])
        if len(adjacentSpaces) == 0:
            path.pop()
            return bestPath
        for space in adjacentSpaces:
            bestPath = findPath(grid, space, target, path, risk, bestPath)

    path.pop()
    #pos.visited = False
    risk -= pos.value
    return bestPath

def findPathBFS(grid: list[list[Position]], pos: Position, target: Position, path: list[Position], risk: float, bestPath: float):
    #printGrid(grid, pos)
    printGrid(grid, path, pos)
    row = pos.row
    col = pos.col

    path.append(pos)
    risk += pos.value
    pos.visited = True
    #print(pos)
    #print(grid)
    #grid[row][col] = pos

    while len(path) > 0:
        nextPos = path.pop(0)
        printGrid(grid, path, pos)

        if nextPos == target:
            #if toPrint:
            #print("\n".join([str(cord) for cord in path]))
            print(risk)
            printGrid(grid, path)
            #paths.append(tuple(path))
            #bestPath = risk
        else:
            row = nextPos.row
            col = nextPos.col
            searchList = [
                                [row - 1, col],
                [row, col - 1],                 [row, col + 1],
                                [row + 1, col]
            ]

            adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited])
            for space in adjacentSpaces:
                space.visited = True
                path.append(space)

    #path.pop()
    #pos.visited = False
    risk -= pos.value

def Dijkstra(grid: list[list[Position]], pos: Position, target: Position):
    loopNum = 0
    searchSpaces = [pos]
    while not target.visited:
        pos = min([space for space in searchSpaces if not space.visited])
        searchSpaces.remove(pos)
        #printGrid(grid, pos=pos)
        print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited])
        for space in adjacentSpaces:
            newDist = space.value + pos.dist
            if newDist < space.dist:
                space.dist = newDist
                space.last = pos
                searchSpaces.append(space)

        pos.visited = True

def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    intGrid = [[math.inf] * (width + 2)] + [[math.inf] + [int(point) for point in list(line)] + [math.inf] for line in input_lines] + [[math.inf] * (width + 2)]
    grid = []
    for rowNum in range(len(intGrid)):
        row = []
        for colNum in range(len(intGrid[0])):
            row.append(Position(rowNum, colNum, intGrid[rowNum][colNum], visited=True if intGrid[rowNum][colNum] == math.inf else False))
        grid.append(row)
    #print(grid)
    #printGrid(grid)

    pos = grid[1][1]
    pos.dist = 0
    target = grid[height][width]
    #findPathBFS(grid, pos, target, [], -pos.value, math.inf)
    Dijkstra(grid, pos, target)
    print(target.dist)

def part2(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    #intGrid = [[math.inf]*(width+2)]+[[math.inf]+[int(point) for point in list(line)]+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]
    intGrid = [[int(point) for point in list(line)] for line in input_lines]
    grid = []
    for ii in range(5):
        for rowNum in range(len(intGrid)):
            row = []
            for jj in range(5):
                for colNum in range(len(intGrid[0])):
                    value = intGrid[rowNum][colNum] + ii + jj
                    while value > 9:
                        value -= 9
                    row.append(Position(rowNum+height*ii+1, colNum+width*jj+1, value, visited=False))
            grid.append(row)
        #print(grid)
    #printGrid(grid, showOnly=False)

    width = len(grid[0])
    height = len(grid)

    grid = np.array(grid)
    grid = np.pad(grid, pad_width=1, mode='constant', constant_values=Position(0, 0, math.inf, visited=True))
    grid = grid.tolist()
    #printGrid(grid, showOnly=False, padWidth=0)

    pos = grid[1][1]
    pos.dist = 0
    target = grid[height][width]
    # findPathBFS(grid, pos, target, [], -pos.value, math.inf)
    Dijkstra(grid, pos, target)
    print(target.dist)

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    start = timeit.default_timer()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    stop = timeit.default_timer()
    print('Time: ', stop-start)

