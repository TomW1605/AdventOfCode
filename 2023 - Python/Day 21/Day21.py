import math
import time

# import cv2
# import numpy as np
# from termcolor import colored
from enum import Enum

# from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

class Type(Enum):
    GARDEN = 1
    ROCK = 2

class Position:
    row: int
    col: int
    type: Type
    visited = False
    occupied = False
    end = False

    def __init__(self, rowNum, colNum, type):
        self.row = rowNum
        self.col = colNum
        self.type = type

    def __str__(self):
        return f'{"Rock" if self.type == Type.ROCK else "Garden"}: ({self.row}, {self.col})'

    def __repr__(self):
        return self.__str__()

# def printGrid(grid: list[list[Position]], pos: Position = None, scale_percent: int = 1000, showOnly: bool = True, padWidth: int = 1, wait: int = 1):
#     height = len(grid)
#     width = len(grid[0])
#
#     imgArray = np.zeros([height-padWidth*2, width-padWidth*2, 3])
#     for row in range(padWidth, height-padWidth):
#         for col in range(padWidth, width-padWidth):
#             pixColour = [0, 0, 0]
#             if grid[row][col].type == Type.GARDEN:
#                 pixColour = [0, 0.5, 0]
#             elif grid[row][col].type == Type.ROCK:
#                 pixColour = [0.5, 0.5, 0.5]
#
#             if grid[row][col].visited:
#                 pixColour = [0, 0, 0.5]
#             if grid[row][col].occupied:
#                 pixColour = [1, 0, 0]
#             if grid[row][col].end:
#                 pixColour = [0.5, 0, 0]
#             imgArray[row-1][col-1] = pixColour
#
#     imgWidth = int((height-2)*scale_percent/100)
#     imgHeight = int((width-2)*scale_percent/100)
#     cv2.imwrite(f"./images/{printGrid.imageNum}.jpg", 255*cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
#     #print(printGrid.imageNum)
#     printGrid.imageNum += 1
#     cv2.imshow('image', cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
#     cv2.waitKey(wait)
#
# printGrid.imageNum = 1

def take_step(grid, pos, max_steps, num_steps=0):
    if num_steps == max_steps:
        pos.end = True
        return grid
    pos.visited = True
    pos.occupied = True
    # printGrid(grid, wait=1)
    # print(num_steps)
    print(sum(sum(1 for space in row if space.end) for row in grid))
    adjacent = [[pos.row-1, pos.col], [pos.row, pos.col-1], [pos.row, pos.col+1], [pos.row+1, pos.col]]
    options = [[row, col] for row, col in adjacent if grid[row][col].type == Type.GARDEN]
    # print(options)

    pos.occupied = False
    for row, col in options:
        take_step(grid, grid[row][col], max_steps, num_steps+1)

def part1(input_lines):
    # print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    str_grid = [["#"]*(width+2)]+[["#"]+[point for point in list(line)]+["#"] for line in input_lines]+[["#"]*(width+2)]
    grid = []
    start = None
    for rowNum in range(len(str_grid)):
        row = []
        for colNum in range(len(str_grid[0])):
            row.append(Position(rowNum, colNum, Type.ROCK if str_grid[rowNum][colNum] == '#' else Type.GARDEN))
            if str_grid[rowNum][colNum] == 'S':
                start = row[-1]
        grid.append(row)
    #print(grid)
    start.occupied = True
    # start.visited = True

    take_step(grid, start, 64)

    print(sum(sum(1 for space in row if space.end) for row in grid))

    # printGrid(grid, wait=0)


def part2(input_lines):
    print(input_lines)


if __name__ == '__main__':
    test = 0
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