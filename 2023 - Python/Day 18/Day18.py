import time

import cv2
import numpy as np
from termcolor import colored

from readFile import readFile

class Position:
    # row: int
    # col: int
    colour = (1, 1, 1)
    inside = False
    corner = False
    dir = ''
    vertical = False

    # dug = False

    def __init__(self, boarder=False):
        self.boarder = boarder

    def __int__(self):
        return int(self.boarder)

    def __str__(self):
        return self.dir if self.dir != '' else '..'#str(int(self.boarder))

    def __repr__(self):
        return self.__str__()

def printGrid(grid, pos=None, inside=None, scale_percent: int = 350, wait: int = 1):
    if inside is None:
        inside = []
    height, width = grid.shape

    block_size = int(scale_percent/100)

    # define the height and width of the merged pictures
    imgArray = np.zeros((block_size*height, block_size*width, 3))

    # imgArray = np.zeros([height, width, 3])
    for row in range(0, height):
        for col in range(0, width):
            # imgArray[row, col] = grid[row, col].colour
            if [row, col] == pos:
                colour_block = np.full((block_size, block_size, 3), (0, 0, 1))
            elif (row, col) in inside:
                colour_block = np.full((block_size, block_size, 3), (0.5, 0.5, 0.5))
            else:
                colour_block = np.full((block_size, block_size, 3), grid[row, col].colour)

            # colour_block[:, [0, -1]] = colour_block[[0, -1]] = (255, 255, 255)

            imgArray[row*block_size:row*block_size+block_size, col*block_size:col*block_size+block_size] = colour_block

    # imgWidth = int(height*(scale_percent/100))
    # imgHeight = int(width*(scale_percent/100))
    # cv2.imwrite(f"./images/{printGrid.imageNum}.jpg", 255*cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    #print(printGrid.imageNum)
    printGrid.imageNum += 1
    cv2.imshow('image', imgArray)  #cv2.resize(np.array(imgArray), (imgWidth, imgHeight), interpolation=cv2.INTER_NEAREST))
    cv2.waitKey(wait)

printGrid.imageNum = 1

def html_to_rgb(html_color):
    # Convert hexadecimal to RGB
    b = int(html_color[0:2], 16)/255
    g = int(html_color[2:4], 16)/255
    r = int(html_color[4:6], 16)/255

    # Return RGB values in the 0 to 255 range
    return r, g, b

def Area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def part1(input_lines):
    print(input_lines)

    instructions = [(line.split(' ')[0], int(line.split(' ')[1]), html_to_rgb(line.split(' ')[2].replace('(#', '').replace(')', ''))) for line in input_lines]
    print(instructions)

    corners = []

    pos = [0, 0]
    grid = np.full((1, 1), Position(True))
    print(grid)
    for instruction in instructions:
        # print(instruction)
        height, width = grid.shape
        # corners.append(pos)
        match instruction[0]:
            case 'R':
                grid[pos[0], pos[1]].dir += 'R'
                extra_width = instruction[1]+pos[1]-width+1
                # print(extra_width)
                if extra_width >= 1:
                    grid = np.hstack((grid, np.array([[Position() for _ in range(extra_width)] for _ in range(height)])))

                for ii in range(1, instruction[1]+1):
                    grid[pos[0], pos[1]+ii].boarder = True
                    grid[pos[0], pos[1]+ii].inside = True
                    grid[pos[0], pos[1]+ii].colour = instruction[2]
                pos[1] = pos[1]+instruction[1]
                grid[pos[0], pos[1]].corner = True
                grid[pos[0], pos[1]].dir += 'L'

            case 'L':
                grid[pos[0], pos[1]].dir += 'L'
                extra_width = (pos[1]-instruction[1])*-1
                # print(extra_width)
                if extra_width >= 1:
                    grid = np.hstack((np.array([[Position() for _ in range(extra_width)] for _ in range(height)]), grid))
                    pos[1] = pos[1]+extra_width

                for ii in range(1, instruction[1]+1):
                    grid[pos[0], pos[1]-ii].boarder = True
                    grid[pos[0], pos[1]-ii].inside = True
                    grid[pos[0], pos[1]-ii].colour = instruction[2]
                pos[1] = pos[1]-instruction[1]
                grid[pos[0], pos[1]].corner = True
                grid[pos[0], pos[1]].dir += 'R'

            case 'D':
                grid[pos[0], pos[1]].dir += 'D'
                extra_height = instruction[1]+pos[0]-height+1
                # print(extra_height)
                if extra_height >= 1:
                    grid = np.vstack((grid, np.array([[Position() for _ in range(width)] for _ in range(extra_height)])))

                for ii in range(1, instruction[1]+1):
                    grid[pos[0]+ii, pos[1]].boarder = True
                    grid[pos[0]+ii, pos[1]].vertical = True
                    grid[pos[0]+ii, pos[1]].inside = True
                    grid[pos[0]+ii, pos[1]].colour = instruction[2]
                pos[0] = pos[0]+instruction[1]
                grid[pos[0], pos[1]].corner = True
                grid[pos[0], pos[1]].dir += 'U'

            case 'U':
                grid[pos[0], pos[1]].dir += 'U'
                extra_height = (pos[0]-instruction[1])*-1
                # print(extra_height)
                if extra_height >= 1:
                    grid = np.vstack((np.array([[Position() for _ in range(width)] for _ in range(extra_height)]), grid))
                    pos[0] = pos[0]+extra_height

                for ii in range(1, instruction[1]+1):
                    grid[pos[0]-ii, pos[1]].boarder = True
                    grid[pos[0]-ii, pos[1]].vertical = True
                    grid[pos[0]-ii, pos[1]].inside = True
                    grid[pos[0]-ii, pos[1]].colour = instruction[2]
                pos[0] = pos[0]-instruction[1]
                grid[pos[0], pos[1]].corner = True
                grid[pos[0], pos[1]].dir += 'D'

        # print(grid)
        # printGrid(grid, pos, wait=1)

    printGrid(grid, wait=0)

    # inside = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row, col].corner:
                corners.append([row, col])
    #         ray = grid[row, :col]
    #         # print(ray)
    #         # corners = [pos for pos in ray if pos.corner]
    #         # for ii in range(0, int(len(corners)/2), 2):
    #         #     corner1 = corners[ii]
    #         #     corner2 = corners[ii+1]
    #         #     if corner1
    #
    #         crosses = (sum(1 for pos in ray if pos.vertical and not pos.corner) +
    #                    int(((sum(1 for pos in ray if pos.corner and pos.dir in ['LD', 'DL']) -
    #                          sum(1 for pos in ray if pos.corner and pos.dir in ['RD', 'DR'])) +
    #                         (sum(1 for pos in ray if pos.corner and pos.dir in ['RU', 'DU']) -
    #                          sum(1 for pos in ray if pos.corner and pos.dir in ['LU', 'UL'])))/2))
    #
    #        # int(
    #        #     (sum(1 for pos in ray if pos.corner and pos.dir == 'U') -
    #        #      sum(1 for pos in ray if pos.corner and pos.dir == 'D')
    #        #      )/2))
    #         # ray.count('│')+int(((ray.count('┐')-ray.count('┌'))+(ray.count('└')-ray.count('┘')))/2)
    #         if crosses%2 == 1:
    #             grid[row, col].inside = True
    #             inside.append((row, col))
    #
    # # print(inside)
    # print(sum(sum(1 for pos in row if pos.inside) for row in grid))

    print(Area(corners))

    printGrid(grid, wait=0)

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

    total_time = time.time()-start_time

    hours = int(total_time/3600)
    minutes = int(total_time/60)
    seconds = total_time%60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
