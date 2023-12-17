import os
import re
import time
from enum import Enum

import cv2
import numpy as np
from PIL import Image
from termcolor import colored

from readFile import readFile
from img_blocks import Block

import sys
sys.setrecursionlimit(3000)
# print(sys.getrecursionlimit())

from itertools import count

def stack_size2a(size=2):
    """Get stack size for caller's frame.
    """
    frame = sys._getframe(size)

    for size in count(size):
        frame = frame.f_back
        if not frame:
            return size

def print_map(light_map, path=[]):
    map_string = ''
    for row in range(len(light_map)):
        for column in range(len(light_map[row])):
            if (row, column) in path:
                map_string += colored(light_map[row][column], 'red', on_color='on_grey')
            else:
                map_string += colored(light_map[row][column])#, on_color='on_blue')
        map_string += '\n'
    # print('\n'.join(map))
    print(map_string)

# class LightMap:
#     img_num = 0

def add_transparent_image(background, foreground, x_offset=None, y_offset=None):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = foreground.shape

    assert bg_channels == 3, f'background image should have exactly 3 channels (RGB). found:{bg_channels}'
    assert fg_channels == 4, f'foreground image should have exactly 4 channels (RGBA). found:{fg_channels}'

    img = np.zeros((bg_h, bg_w, bg_channels), np.uint8)

    # center by default
    if x_offset is None: x_offset = (bg_w - fg_w) // 2
    if y_offset is None: y_offset = (bg_h - fg_h) // 2

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w < 1 or h < 1: return

    # clip foreground and background images to the overlapping regions
    bg_x = max(0, x_offset)
    bg_y = max(0, y_offset)
    fg_x = max(0, x_offset * -1)
    fg_y = max(0, y_offset * -1)
    foreground = foreground[fg_y:fg_y + h, fg_x:fg_x + w]
    background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

    # separate alpha and color channels from the foreground image
    foreground_colors = foreground[:, :, :3]
    alpha_channel = foreground[:, :, 3] / 255  # 0-255 => 0.0-1.0

    # construct an alpha_mask that matches the image shape
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    # combine the background with the overlay image weighted by alpha
    composite = background_subsection * (1 - alpha_mask) + foreground_colors * alpha_mask

    # overwrite the section of the background image that has been updated
    img[bg_y:bg_y + h, bg_x:bg_x + w] = composite

    return img


def show_map(light_map):
    block_size = 8

    # define the height and width of the merged pictures
    img = np.zeros((block_size * len(light_map), block_size * len(light_map[0]), 3), np.uint8)
    # img = np.zeros((block_height, block_width, 3), np.uint8)

    # paste each img to the right place
    # img[0:h1, 0:w1] = img1
    # img[0:h2, w1:] = img2

    for row in range(len(light_map)):
        for column in range(len(light_map[row])):
            img[row*block_size:row*block_size+block_size, column*block_size:column*block_size+block_size] = light_map[row][column].img

    folder = "./images/"

    os.makedirs(folder, exist_ok=True)

    existing_img = next(os.walk(folder))[2]
    existing_img.sort(key=lambda f: int(re.sub('\D', '', f)))
    if len(existing_img) > 0:
        img_num = int(existing_img[-1].split(".")[0])+1
    else:
        img_num = 1

    cv2.imwrite(f"./images/{img_num}.jpg", img)
    # cv2.imshow('img', img)
    # cv2.waitKey(1)

class Type(Enum):
    WALL = 0
    EMPTY = 1
    MIRROR_L = 2
    MIRROR_R = 3
    SPLITTER_H = 4
    SPLITTER_V = 5

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4

class Space:
    energised = False
    type = Type.EMPTY
    cords = (0, 0)
    img = Block.Empty.NONE
    # directions = list()

    #np.uint8(alpha*(img1)+beta*(img2))

    def __init__(self, type, cords):
        self.type = type
        self.cords = cords

        self.directions = []

        match self.type:
            case Type.MIRROR_L:
                self.img = Block.Mirror.Left.NONE
            case Type.MIRROR_R:
                self.img = Block.Mirror.Right.NONE
            case Type.SPLITTER_H:
                self.img = Block.Splitter.Horizontal.NONE
            case Type.SPLITTER_V:
                self.img = Block.Splitter.Vertical.NONE
            case Type.WALL:
                self.img = Block.WALL
                self.directions = [
                    Direction.LEFT,
                    Direction.RIGHT,
                    Direction.TOP,
                    Direction.BOTTOM
                ]

    def __str__(self):
        return str(self.directions)

    def __repr__(self):
        return self.__str__()

    def add_light(self, direction, light_map: list[list['Space']]):
        if direction in self.directions:
            return
        # print(stack_size2a())
        self.directions.append(direction)
        if self.type == Type.EMPTY:
            if direction in [Direction.LEFT, direction.RIGHT]:
                self.directions.append(Direction.LEFT)
                self.directions.append(Direction.RIGHT)
            elif direction in [Direction.TOP, direction.BOTTOM]:
                self.directions.append(Direction.TOP)
                self.directions.append(Direction.BOTTOM)
        self.energised = True
        # show_map(light_map)
        match direction:
            case Direction.LEFT:
                match self.type:
                    case Type.MIRROR_L:
                        self.img = add_transparent_image(self.img, Block.Mirror.Left.LEFT)# = np.uint8(self.img+Block.Mirror.Left.LEFT)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)
                    case Type.MIRROR_R:
                        self.img = add_transparent_image(self.img, Block.Mirror.Right.LEFT)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)
                    case Type.SPLITTER_H:
                        self.img = add_transparent_image(self.img, Block.Splitter.Horizontal.LEFT)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)
                    case Type.SPLITTER_V:
                        self.img = add_transparent_image(self.img, Block.Splitter.Vertical.LEFT)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)
                    case Type.EMPTY:
                        self.img = add_transparent_image(self.img, Block.Empty.HORIZONTAL)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)

            case Direction.RIGHT:
                match self.type:
                    case Type.MIRROR_L:
                        self.img = add_transparent_image(self.img, Block.Mirror.Left.RIGHT)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)
                    case Type.MIRROR_R:
                        self.img = add_transparent_image(self.img, Block.Mirror.Right.RIGHT)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)
                    case Type.SPLITTER_H:
                        self.img = add_transparent_image(self.img, Block.Splitter.Horizontal.RIGHT)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)
                    case Type.SPLITTER_V:
                        self.img = add_transparent_image(self.img, Block.Splitter.Vertical.RIGHT)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)
                    case Type.EMPTY:
                        self.img = add_transparent_image(self.img, Block.Empty.HORIZONTAL)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)

            case Direction.TOP:
                match self.type:
                    case Type.MIRROR_L:
                        self.img = add_transparent_image(self.img, Block.Mirror.Left.TOP)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)
                    case Type.MIRROR_R:
                        self.img = add_transparent_image(self.img, Block.Mirror.Right.TOP)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)
                    case Type.SPLITTER_H:
                        self.img = add_transparent_image(self.img, Block.Splitter.Horizontal.TOP)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)
                    case Type.SPLITTER_V:
                        self.img = add_transparent_image(self.img, Block.Splitter.Vertical.TOP)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)
                    case Type.EMPTY:
                        self.img = add_transparent_image(self.img, Block.Empty.VERTICAL)
                        light_map[self.cords[0]+1][self.cords[1]].add_light(Direction.TOP, light_map)

            case Direction.BOTTOM:
                match self.type:
                    case Type.MIRROR_L:
                        self.img = add_transparent_image(self.img, Block.Mirror.Left.BOTTOM)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)
                    case Type.MIRROR_R:
                        self.img = add_transparent_image(self.img, Block.Mirror.Right.BOTTOM)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)
                    case Type.SPLITTER_H:
                        self.img = add_transparent_image(self.img, Block.Splitter.Horizontal.BOTTOM)
                        light_map[self.cords[0]][self.cords[1]-1].add_light(Direction.RIGHT, light_map)
                        light_map[self.cords[0]][self.cords[1]+1].add_light(Direction.LEFT, light_map)
                    case Type.SPLITTER_V:
                        self.img = add_transparent_image(self.img, Block.Splitter.Vertical.BOTTOM)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)
                    case Type.EMPTY:
                        self.img = add_transparent_image(self.img, Block.Empty.VERTICAL)
                        light_map[self.cords[0]-1][self.cords[1]].add_light(Direction.BOTTOM, light_map)

def part1(input_lines):
    # show_map(input_lines)
    light_map = [[Space(Type.EMPTY, (row, column)) for column in range(len(input_lines[row]))] for row in range(len(input_lines))]
    for row in range(len(input_lines)):
        for column in range(len(input_lines[row])):
            match input_lines[row][column]:
                case '\\':
                    light_map[row][column] = Space(Type.MIRROR_L, (row, column))
                case '/':
                    light_map[row][column] = Space(Type.MIRROR_R, (row, column))
                case '-':
                    light_map[row][column] = Space(Type.SPLITTER_H, (row, column))
                case '|':
                    light_map[row][column] = Space(Type.SPLITTER_V, (row, column))
                case '█':
                    light_map[row][column] = Space(Type.WALL, (row, column))

    light_map[1][1].add_light(Direction.LEFT, light_map)

    print(sum(sum(space.energised for space in row) for row in light_map))

def part2(input_lines):
    # print(input_lines)

    max_energised = 0
    for ii in range(1, len(input_lines)-1):
        light_map = [[Space(Type.EMPTY, (row, column)) for column in range(len(input_lines[row]))] for row in range(len(input_lines))]
        for row in range(len(input_lines)):
            for column in range(len(input_lines[row])):
                match input_lines[row][column]:
                    case '\\':
                        light_map[row][column] = Space(Type.MIRROR_L, (row, column))
                    case '/':
                        light_map[row][column] = Space(Type.MIRROR_R, (row, column))
                    case '-':
                        light_map[row][column] = Space(Type.SPLITTER_H, (row, column))
                    case '|':
                        light_map[row][column] = Space(Type.SPLITTER_V, (row, column))
                    case '█':
                        light_map[row][column] = Space(Type.WALL, (row, column))

        light_map[ii][1].add_light(Direction.LEFT, light_map)

        total = sum(sum(space.energised for space in row) for row in light_map)
        print(total)
        if total > max_energised:
            max_energised = total

        light_map[ii][-1].add_light(Direction.RIGHT, light_map)

        total = sum(sum(space.energised for space in row) for row in light_map)
        print(total)
        if total > max_energised:
            max_energised = total

    for ii in range(1, len(input_lines[0])-1):
        light_map = [[Space(Type.EMPTY, (row, column)) for column in range(len(input_lines[row]))] for row in range(len(input_lines))]
        for row in range(len(input_lines)):
            for column in range(len(input_lines[row])):
                match input_lines[row][column]:
                    case '\\':
                        light_map[row][column] = Space(Type.MIRROR_L, (row, column))
                    case '/':
                        light_map[row][column] = Space(Type.MIRROR_R, (row, column))
                    case '-':
                        light_map[row][column] = Space(Type.SPLITTER_H, (row, column))
                    case '|':
                        light_map[row][column] = Space(Type.SPLITTER_V, (row, column))
                    case '█':
                        light_map[row][column] = Space(Type.WALL, (row, column))

        light_map[1][ii].add_light(Direction.TOP, light_map)

        total = sum(sum(space.energised for space in row) for row in light_map)
        print(total)
        if total > max_energised:
            max_energised = total

        light_map[-1][ii].add_light(Direction.BOTTOM, light_map)

        total = sum(sum(space.energised for space in row) for row in light_map)
        print(total)
        if total > max_energised:
            max_energised = total

    print(max_energised)


if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    inputLines = ['█'*len(inputLines[0])]+inputLines+['█'*len(inputLines[0])]

    for ii in range(len(inputLines)):
        inputLines[ii] = '█'+inputLines[ii]+'█'

    # replacements = {
    #     '-': '─',
    #     '|': '│',
    #     '/': '╱',
    #     '\\': '╲',
    #     '.': '░',
    # }
    #
    # for ii in range(len(inputLines)):
    #     inputLines[ii] = inputLines[ii].translate(str.maketrans(replacements))

    inputLines = [list(line) for line in inputLines]

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")