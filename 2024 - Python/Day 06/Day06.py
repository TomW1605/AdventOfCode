import os
import re
import time

from enum import Enum

import cv2
import numpy as np
from pydantic import BaseModel, computed_field, Field, ConfigDict
from img_blocks import Block

class Direction(Enum):
    UP = "^"
    DOWN = "V"
    LEFT = "<"
    RIGHT = ">"

    def rotate_right(self):
        match self.name:
            case "UP":
                return Direction.RIGHT
            case "DOWN":
                return Direction.LEFT
            case "LEFT":
                return Direction.UP
            case "RIGHT":
                return Direction.DOWN

class Guard(BaseModel):
    X: int
    Y: int
    direction: Direction

    @computed_field
    @property
    def position(self) -> list[int]:
        return [self.X, self.Y]

    @computed_field
    @property
    def next_step(self) -> list[int]:
        next_step = [self.X, self.Y]
        match self.direction:
            case Direction.UP:
                next_step[1] -= 1
            case Direction.DOWN:
                next_step[1] += 1
            case Direction.LEFT:
                next_step[0] -= 1
            case Direction.RIGHT:
                next_step[0] += 1
        return next_step

    def move(self, grid):
        next_step = self.next_step
        if next_step[0] >= len(grid) or next_step[1] >= len(grid[0]):
            grid[self.Y][self.X].type = "X"
            return False
        if grid[next_step[1]][next_step[0]].is_obstacle:
            self.direction = self.direction.rotate_right()
            grid[self.Y][self.X].type = self.direction.value
        else:
            grid[self.Y][self.X].type = "X"
            match self.direction:
                case Direction.UP:
                    grid[self.Y][self.X].add_image(Block.Empty.TOP)
                case Direction.DOWN:
                    grid[self.Y][self.X].add_image(Block.Empty.BOTTOM)
                case Direction.LEFT:
                    grid[self.Y][self.X].add_image(Block.Empty.LEFT)
                case Direction.RIGHT:
                    grid[self.Y][self.X].add_image(Block.Empty.RIGHT)
            self.X = next_step[0]
            self.Y = next_step[1]
            grid[self.Y][self.X].type = self.direction.value
            match self.direction:
                case Direction.UP:
                    grid[self.Y][self.X].add_image(Block.Empty.BOTTOM)
                case Direction.DOWN:
                    grid[self.Y][self.X].add_image(Block.Empty.TOP)
                case Direction.LEFT:
                    grid[self.Y][self.X].add_image(Block.Empty.RIGHT)
                case Direction.RIGHT:
                    grid[self.Y][self.X].add_image(Block.Empty.LEFT)
            # grid[self.Y][self.X].add_image(Block.GUARD)
        return True

class MapPoint(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    type: str
    X: int
    Y: int
    img: np.ndarray[np.uint8] = Field(default_factory=lambda data: Block.WALL if data["type"] == "#" else Block.Empty.NONE)

    @computed_field
    @property
    def visited(self) -> bool:
        return self.type == "X"

    @computed_field
    @property
    def is_obstacle(self) -> bool:
        return self.type == "#"

    @computed_field
    @property
    def is_guard(self) -> bool:
        return self.type in ["^", "V", "<", ">"]

    def __eq__(self, other):
        if not isinstance(other, MapPoint):
            return False
        return self.X == other.X and self.Y == other.Y

    def add_image(self, foreground, x_offset=None, y_offset=None):
        background = self.img
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

        self.img = img

class Map(BaseModel):
    grid: list[list[MapPoint]]

    def __str__(self):
        return "\n".join(["".join([point.type for point in line]) for line in self.grid])

    def show(self):
        block_size = 5
        grid = self.grid

        # define the height and width of the merged pictures
        img = np.zeros((block_size * len(grid), block_size * len(grid[0]), 3), np.uint8)

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                img[row*block_size:row*block_size+block_size, column*block_size:column*block_size+block_size] = grid[row][column].img

        folder = "./images/"

        os.makedirs(folder, exist_ok=True)

        existing_img = next(os.walk(folder))[2]
        existing_img.sort(key=lambda f: int(re.sub('\D', '', f)))
        if len(existing_img) > 0:
            img_num = int(existing_img[-1].split(".")[0])+1
        else:
            img_num = 1

        cv2.imwrite(f"images/{img_num:>04}.jpg", img)
        cv2.imshow('img', img)
        cv2.waitKey(1)

def part1(input_lines):
    map = Map(grid=[[MapPoint(type=input_lines[y][x], X=x, Y=y) for x in range(len(input_lines[y]))] for y in range(len(input_lines))])
    grid = map.grid
    guard = None
    for line in grid:
        for point in line:
            if point.is_guard:
                guard = Guard(X=line.index(point), Y=grid.index(line), direction=Direction(point.type))
                break
        if guard:
            break

    # print(map, "\n")
    map.show()
    while guard.move(grid):
        # print(map, "\n")
        map.show()
    visited_total = sum([1 for line in grid for point in line if point.visited])
    print(visited_total)

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 1
    part = 1

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
