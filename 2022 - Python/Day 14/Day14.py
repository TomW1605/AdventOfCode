from readFile import readFile
import math
from dataclasses import dataclass
import cv2
import numpy as np
from enum import Enum

class Type(Enum):
    AIR = 1
    ROCK = 2
    SAND = 3

@dataclass
class Point:
    x: int
    y: int
    type: Type = Type.AIR

    def _is_valid_operand(self, other):
        return hasattr(other, "row") and hasattr(other, "col") and hasattr(other, "height")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        #return f"({self.row}, {self.col}): ({self.height}, {self.visited})"
        return f"{self.type}"

    def __repr__(self):
        #return str(mapRange(self.height, 1, 26, 0, 255))
        return self.__str__()

    def __int__(self):
        return int(self.type.value)

    def __float__(self):
        return float(self.__int__())

def print_grid(grid: list[list[Point]], x_offset: int = 0, point: Point = None, scale_percent: int = 250, pad_width: int = 0, term_print: bool = False):
    height = len(grid)
    width = len(grid[0])
    x_offset = x_offset-2

    img_array = np.zeros([height-pad_width*2, width-pad_width*2-x_offset, 3])
    for row in range(pad_width, height-pad_width):
        for col in range(pad_width+x_offset, width-pad_width):
            pix_colour = [0, 0, 0]
            print_char = " "
            if grid[row][col].type == Type.SAND:
                pix_colour = [0.5647058823529412, 0.8156862745098039, 1]
                print_char = "░"
            if grid[row][col].type == Type.ROCK:
                pix_colour = [0.5, 0.5, 0.5]
                print_char = "█"
            if point is not None and grid[row][col] == point:
                pix_colour = [0, 0, 1]
                print_char = "█"
            img_array[row-1][col-1-x_offset] = pix_colour
            if term_print:
                print(print_char, end="")
        if term_print:
            print()
    if term_print:
        print()

    img_width = max(int((width-2-x_offset)*scale_percent/100), 1)
    img_height = max(int((height-2)*scale_percent/100), 1)
    #cv2.imwrite(f"./images/{print_grid.imageNum}.jpg", 255*cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    print_grid.imageNum += 1
    cv2.imshow('image', cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(1)
print_grid.imageNum = 1


def make_grid(input_lines):
    grid = np.array([[Point(0, 0, Type.AIR)]])
    x_offset = 500
    bottom = 0
    for line in input_lines:
        points = line.split(" -> ")
        for ii in range(1, len(points)):
            x, y = points[ii-1].split(",")
            start = Point(int(x), int(y), Type.ROCK)
            x, y = points[ii].split(",")
            end = Point(int(x), int(y), Type.ROCK)

            if grid.shape[1] <= start.x:
                grid = np.pad(grid, ((0, 0), (0, start.x-grid.shape[1]+1)), constant_values=Point(-1, -1, Type.AIR))
            if grid.shape[0] <= start.y:
                grid = np.pad(grid, ((0, start.y-grid.shape[0]+1), (0, 0)), constant_values=Point(-1, -1, Type.AIR))

            if x_offset > start.x:
                x_offset = start.x
            if bottom < start.y:
                bottom = start.y

            grid[start.y][start.x] = start
            #print_grid(grid, x_offset, start)

            if start.x == end.x:
                for yy in range(start.y, end.y, -1 if end.y < start.y else 1):
                    new_point = Point(start.x, yy, Type.ROCK)
                    if grid.shape[0] <= new_point.y:
                        grid = np.pad(grid, ((0, new_point.y-grid.shape[0]+1), (0, 0)), constant_values=Point(-1, -1, Type.AIR))

                    if x_offset > new_point.x:
                        x_offset = new_point.x
                    if bottom < new_point.y:
                        bottom = new_point.y

                    grid[new_point.y][new_point.x] = new_point
                    #print_grid(grid, x_offset, new_point)

                if grid.shape[0] <= end.y:
                    grid = np.pad(grid, ((0, end.y-grid.shape[0]+1), (0, 0)), constant_values=Point(-1, -1, Type.AIR))

                if x_offset > end.x:
                    x_offset = end.x
                if bottom < end.y:
                    bottom = end.y

                grid[end.y][end.x] = end
                #print_grid(grid, x_offset, end)

            if start.y == end.y:
                for xx in range(start.x, end.x, -1 if end.x < start.x else 1):
                    new_point = Point(xx, start.y, Type.ROCK)
                    if grid.shape[1] <= new_point.x:
                        grid = np.pad(grid, ((0, 0), (0, new_point.x-grid.shape[1]+1)), constant_values=Point(-1, -1, Type.AIR))

                    if x_offset > new_point.x:
                        x_offset = new_point.x
                    if bottom < new_point.y:
                        bottom = new_point.y

                    grid[new_point.y][new_point.x] = new_point
                    #print_grid(grid, x_offset, new_point)

                if grid.shape[1] <= end.x:
                    grid = np.pad(grid, ((0, 0), (0, end.x-grid.shape[1]+1)), constant_values=Point(-1, -1, Type.AIR))

                if x_offset > end.x:
                    x_offset = end.x
                if bottom < end.y:
                    bottom = end.y

                grid[end.y][end.x] = end
                #print_grid(grid, x_offset, end)

            #print(grid)
            #print()
    return grid, x_offset, bottom


def part1(input_lines):
    print(input_lines)
    grid, x_offset, bottom = make_grid(input_lines)

    ii = 0
    while True:
        sand = Point(500, 0, Type.SAND)

        if grid.shape[1] <= sand.x+2:
            grid = np.pad(grid, ((0, 0), (0, (sand.x-grid.shape[1])+4)), constant_values=Point(-1, -1, Type.AIR))
        if grid.shape[0] <= sand.y+2:
            grid = np.pad(grid, ((0, (sand.y-grid.shape[0])+4), (0, 0)), constant_values=Point(-1, -1, Type.AIR))

        grid[sand.y][sand.x] = sand
        while True:
            if grid.shape[1] <= sand.x+1:
                grid = np.pad(grid, ((0, 0), (0, sand.x-grid.shape[1]+2)), constant_values=Point(-1, -1, Type.AIR))
            if grid.shape[0] <= sand.y+1:
                grid = np.pad(grid, ((0, sand.y-grid.shape[0]+2), (0, 0)), constant_values=Point(-1, -1, Type.AIR))

            if grid[sand.y+1][sand.x].type == Type.AIR:
                sand.y += 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x] = Point(sand.x, sand.y-1, Type.AIR)
            elif grid[sand.y+1][sand.x-1].type == Type.AIR:
                sand.y += 1
                sand.x -= 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x+1] = Point(sand.x+1, sand.y-1, Type.AIR)
            elif grid[sand.y+1][sand.x+1].type == Type.AIR:
                sand.y += 1
                sand.x += 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x-1] = Point(sand.x-1, sand.y-1, Type.AIR)
            else:
                break

            if sand.y > bottom:
                break

            """if sand.y >= 150:
                print_grid(grid, x_offset)"""

        if sand.y > bottom:
            break

        ii += 1
    print_grid(grid, x_offset)

    print(ii)
    input()

def part2(input_lines):
    print(input_lines)
    grid, x_offset, bottom = make_grid(input_lines)
    grid = np.pad(grid, ((0, 0), (0, 700-grid.shape[1])), constant_values=Point(-1, -1, Type.AIR))

    grid = np.pad(grid, ((0, 1), (0, 0)), constant_values=Point(-1, -1, Type.AIR))
    grid = np.pad(grid, ((0, 1), (0, 0)), constant_values=Point(-1, -1, Type.ROCK))

    ii = 0
    run = True
    while run:
        sand = Point(500, 0, Type.SAND)

        if grid.shape[1] <= sand.x+2:
            grid = np.pad(grid, ((0, 0), (0, (sand.x-grid.shape[1])+4)), mode="edge")#, constant_values=Point(-1, -1, Type.AIR))
        if grid.shape[0] <= sand.y+2:
            grid = np.pad(grid, ((0, (sand.y-grid.shape[0])+4), (0, 0)), mode="edge")#, constant_values=Point(-1, -1, Type.AIR))

        grid[sand.y][sand.x] = sand
        moved = False
        while True:
            if grid.shape[1] <= sand.x+1:
                grid = np.pad(grid, ((0, 0), (0, sand.x-grid.shape[1]+2)), mode="edge")#, constant_values=Point(-1, -1, Type.AIR))
            if grid.shape[0] <= sand.y+1:
                grid = np.pad(grid, ((0, sand.y-grid.shape[0]+2), (0, 0)), mode="edge")#, constant_values=Point(-1, -1, Type.AIR))

            if grid[sand.y+1][sand.x].type == Type.AIR:
                sand.y += 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x] = Point(sand.x, sand.y-1, Type.AIR)
                moved = True
            elif grid[sand.y+1][sand.x-1].type == Type.AIR:
                sand.y += 1
                sand.x -= 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x+1] = Point(sand.x+1, sand.y-1, Type.AIR)
                moved = True
            elif grid[sand.y+1][sand.x+1].type == Type.AIR:
                sand.y += 1
                sand.x += 1
                grid[sand.y][sand.x] = sand
                grid[sand.y-1][sand.x-1] = Point(sand.x-1, sand.y-1, Type.AIR)
                moved = True
            else:
                if not moved:
                    run = False
                break

            """if sand.y > bottom:
                break"""

        """if ii >= 901:
            print_grid(grid, 350)"""

        """if sand.y > bottom:
            break"""

        ii += 1
    print_grid(grid, 320)

    print(ii)
    print()


if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = list(set(readFile("testInput.txt")))
    else:
        inputLines = list(set(readFile("input.txt")))

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

