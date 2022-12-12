import math
from dataclasses import dataclass
import cv2
import numpy as np
from termcolor import colored

from readFile import readFile

def mapRange(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Position:
    pass

@dataclass
class Position:
    row: int
    col: int
    height: float = 0
    dist: float = math.inf
    visited: bool = False
    last: Position = None

    def _is_valid_operand(self, other):
        return hasattr(other, "row") and hasattr(other, "col") and hasattr(other, "height")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.col == other.col and self.row == other.row

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.height < other.dist

    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.height > other.height

    def __str__(self):
        #return f"({self.row}, {self.col}): ({self.height}, {self.visited})"
        return f"{self.height}"

    def __repr__(self):
        #return str(mapRange(self.height, 1, 26, 0, 255))
        return self.__str__()

    def __int__(self):
        return int(self.height) if self.height < math.inf else 0

    def __float__(self):
        return float(self.height)


def print_grid(grid: list[list[Position]], path: list[Position] = None, pos: Position = None, scale_percent: int = 2000, show_only: bool = True, pad_width: int = 1, search_list: list[Position] = None):
    height = len(grid)
    width = len(grid[0])

    genPath = None
    if path is None and pos is not None:
        genPath = []
        last = pos.last
        while last is not None:
            genPath.append(last)
            last = last.last

    img_array = np.zeros([height-pad_width*2, width-pad_width*2, 3])
    for row in range(pad_width, height-pad_width):
        for col in range(pad_width, width-pad_width):
            colour = 'green'
            pix_colour = [mapRange(grid[row][col].height, 1, 26, 0.1, 1), mapRange(grid[row][col].height, 1, 26, 0.1, 1), mapRange(grid[row][col].height, 1, 26, 0.1, 1)]
            if path is not None and grid[row][col] in path or grid[row][col].visited:
                colour = 'red'
                pix_colour = [0, 0, mapRange(grid[row][col].height, 1, 26, 0.1, 1)]
            if search_list is not None and grid[row][col] in search_list:
                colour = 'blue'
                pix_colour = [mapRange(grid[row][col].height, 1, 26, 0.1, 1), 0, 0]
            if grid[row][col] == pos or genPath is not None and grid[row][col] in genPath:
                colour = 'blue'
                pix_colour = [0, mapRange(grid[row][col].height, 1, 26, 0.1, 1), 0]
            img_array[row-1][col-1] = pix_colour
            if not show_only:
                print(colored(str(grid[row][col].height), colour), end='')
        if not show_only:
            print("")
    if not show_only:
        print("")

    img_width = int((width-2)*scale_percent/100)
    img_height = int((height-2)*scale_percent/100)
    cv2.imwrite(f"./images/{print_grid.imageNum}.jpg", 255*cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    print_grid.imageNum += 1
    cv2.imshow('image', cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(1)
print_grid.imageNum = 1

max_height = 0
def Dijkstra(grid: list[list[Position]], pos: Position, target: Position):
    loopNum = 0
    searchSpaces = [pos]
    while not target.visited:
        searchSpaces = [space for space in searchSpaces if not space.visited]
        pos = max(searchSpaces)
        searchSpaces.remove(pos)
        print_grid(grid, pos=pos, search_list=searchSpaces)
        #print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited], reverse=True)
        for space in adjacentSpaces:
            if space.height in [pos.height, pos.height+1] or space.height < pos.height:
                space.dist = pos.dist+1
                space.last = pos
                searchSpaces.append(space)
                searchSpaces = [space for space in searchSpaces if not (space.height < pos.height and space not in adjacentSpaces)]

        pos.visited = True


def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    pos = None
    target = None

    int_grid = [[math.inf]*(width+2)]+[[math.inf]+[ord(point)-96 for point in list(line)]+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]
    grid = []
    for row_num in range(len(int_grid)):
        row = []
        for col_num in range(len(int_grid[0])):
            row.append(Position(row_num, col_num, int_grid[row_num][col_num], visited=True if int_grid[row_num][col_num] == math.inf else False))
            if int_grid[row_num][col_num] == -13:
                pos = row[col_num]
                pos.height = 12
                pos.dist = 0
            if int_grid[row_num][col_num] == -27:
                target = row[col_num]
                target.height = 26
        grid.append(row)
    print(grid)
    print_grid(grid)

    #findPathBFS(grid, pos, target, [], -pos.value, math.inf)
    Dijkstra(grid, pos, target)
    print(target.dist)


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
