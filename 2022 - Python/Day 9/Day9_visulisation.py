from typing import List

import cv2
import numpy as np
from termcolor import colored
from tqdm import tqdm

from readFile import readFile

class Knot:
    x = 0
    y = 0
    name = ""

    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Knot):
            if other.x == self.x and other.y == self.y:
                return True
        return False

    def __hash__(self):
        return hash(repr(self))


def adjacent(knot_1: Knot, knot_2: Knot):
    if knot_2.x in [knot_1.x, knot_1.x + 1, knot_1.x - 1] and knot_2.y in [knot_1.y, knot_1.y + 1, knot_1.y - 1]:
        return True
    return False


def gen_grid(cur_knots: list[Knot], visited: set[tuple[int, int]], max_point, min_point):
    grid = []
    for yy in range(max_point[1]+1, min_point[1], -1):
        line = []
        for xx in range(min_point[0], max_point[0]+1):
            #print([xx, yy])
            if Knot(xx, yy-1) in cur_knots:
                line.append(cur_knots[cur_knots.index(Knot(xx, yy-1))].name)
                #print(cur_knots[cur_knots.index(Knot(xx, yy-1))].name, end="")
            elif [xx, yy-1] == [0, 0]:
                line.append("s")
                #print("s", end="")
            elif (xx, yy-1) in visited:
                line.append("#")
                #print("#", end="")
            else:
                line.append(".")
                #print(".", end="")
        grid.append(line)
        #print(line)
    return grid


def print_grid(grid, scale_percent: int = 1000, show_only: bool = True, pad_width: int = 1):
    grid = np.pad(grid, pad_width=pad_width, mode='constant', constant_values=0)
    height = len(grid)
    width = len(grid[0])

    img_array = np.zeros([height - pad_width * 2, width - pad_width * 2, 3])
    for row in range(pad_width, height - pad_width):
        for col in range(pad_width, width - pad_width):
            colour = 'green'
            pix_colour = [0, 1, 0]
            if grid[row][col] == "H":
                colour = 'blue'
                pix_colour = [1, 0, 0]
            if grid[row][col] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                colour = 'red'
                pix_colour = [0, 0, 1]
            if grid[row][col] in ["#", "s"]:
                colour = 'lightblue'
                pix_colour = [1, 0.7, 0]
            img_array[row-1][col-1] = pix_colour
            if not show_only:
                print(colored(str(grid[row][col].value), colour), end='')
        if not show_only:
            print("")
    if not show_only:
        print("")

    img_width = int((width-2)*scale_percent/100)
    img_height = int((height-2)*scale_percent/100)
    cv2.imwrite(f"./images/{print_grid.imageNum}.jpg", 255*cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    print_grid.imageNum += 1
    cv2.imshow('image', 255*cv2.resize(np.array(img_array), (img_width, img_height), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(1)


print_grid.imageNum = 1


def part_1_and_2(input_lines, knots):
    print(input_lines)
    visited = {(0, 0)}
    max_point = [0, 0]
    min_point = [0, 0]

    for line in input_lines:
        direction, distance = line.split()
        for _ in range(int(distance)):
            if direction == "R":
                knots[0].x += 1
            elif direction == "L":
                knots[0].x -= 1
            elif direction == "U":
                knots[0].y += 1
            elif direction == "D":
                knots[0].y -= 1

            if knots[0].x > max_point[0]:
                max_point[0] = knots[0].x
            if knots[0].y > max_point[1]:
                max_point[1] = knots[0].y

            if knots[0].x < min_point[0]:
                min_point[0] = knots[0].x
            if knots[0].y < min_point[1]:
                min_point[1] = knots[0].y

    knots[0] = Knot(0, 0, "H")

    print_grid(gen_grid(knots, visited, max_point, min_point))

    for jj in tqdm(range(0, len(input_lines)), leave=False, unit="moves", unit_scale=False):
        line = input_lines[jj]
        direction, distance = line.split()
        for _ in range(int(distance)):
            if direction == "R":
                knots[0].x += 1
            elif direction == "L":
                knots[0].x -= 1
            elif direction == "U":
                knots[0].y += 1
            elif direction == "D":
                knots[0].y -= 1

            #print(knots)
            #print_grid(knots, max_point, min_point)
            tqdm(range(1, len(knots)), leave=False, unit="fish", unit_scale=True)
            for ii in range(1, len(knots)):
                if not adjacent(knots[ii-1], knots[ii]):
                    #print("not adjacent")

                    if knots[ii].x > knots[ii-1].x:
                        knots[ii].x -= 1

                    if knots[ii].y > knots[ii-1].y:
                        knots[ii].y -= 1

                    if knots[ii].x < knots[ii-1].x:
                        knots[ii].x += 1

                    if knots[ii].y < knots[ii-1].y:
                        knots[ii].y += 1

                    #print_grid(knots, max_point, min_point)

                    if ii == len(knots)-1:
                        visited.add((knots[ii].x, knots[ii].y))

        print_grid(gen_grid(knots, visited, max_point, min_point))
        #print(visited)
        #print()

    print(len(visited))


if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        knots = [Knot(0, 0, "H"), Knot(0, 0, "T")]
        part_1_and_2(inputLines, knots)
    elif part == 2:
        knots = [Knot(0, 0, "H"), Knot(0, 0, "1"), Knot(0, 0, "2"), Knot(0, 0, "3"), Knot(0, 0, "4"),
                 Knot(0, 0, "5"), Knot(0, 0, "6"), Knot(0, 0, "7"), Knot(0, 0, "8"), Knot(0, 0, "9")]
        part_1_and_2(inputLines, knots)

