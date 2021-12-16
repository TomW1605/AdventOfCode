import math
import os
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

@dataclass
class Position:
    row: int
    col: int
    value: float = 0
    visited: bool = False

    def _is_valid_operand(self, other):
        return hasattr(other, "row") and hasattr(other, "col") and hasattr(other, "value")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.col == other.col and self.row == other.row
    
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.value < other.value

    def __str__(self):
        return f"({self.row}, {self.col}): ({self.value}, {self.visited})"

    def __int__(self):
        return int(self.value) if self.value < math.inf else 0

    def __float__(self):
        return float(self.value)

def printGrid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None):
    height = len(grid)
    width = len(grid[0])
    img = Image.new('RGB', (width, height), color='green')
    pixels = img.load()
    for row in range(1, height-1):
        for col in range(1, width-1):
            colour = 'green'
            if path is not None and grid[row][col] in path:
                colour = 'red'
            if grid[row][col] == pos:
                colour = 'blue'
            pixels[row, col] = colour
            print(colored(str(grid[row][col].value), colour), end='')
        print("")
    print("")
    #print("\r"*height, end='')
    #os.system('cls')
    #print("\033[H\033[J", end="")
    #print(chr(27) + "[2J")
    #plt.imshow([[1 if jj in path else 0 for jj in ii] for ii in grid], cmap="gray")
    #plt.pause(0.05)


def findPath(grid: list[list[Position]], pos: Position, target: Position, path: list[Position], risk: float, bestPath: float):
    #print(pos)
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

def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    intGrid = [[math.inf] * (width + 2)] + [[math.inf] + [int(point) for point in list(line)] + [math.inf] for line in input_lines] + [[math.inf] * (width + 2)]
    grid = []
    for rowNum in range(len(intGrid)):
        row = []
        for colNum in range(len(intGrid[0])):
            row.append(Position(rowNum, colNum, intGrid[rowNum][colNum], True if intGrid[rowNum][colNum] == math.inf else False))
        grid.append(row)
    #print(grid)
    printGrid(grid)

    pos = grid[1][1]
    target = Position(width, height)
    bestPath = findPath(grid, pos, target, [], -pos.value, math.inf)
    print(bestPath)
    plt.show()

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 0
    part = 1

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

