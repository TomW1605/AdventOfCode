import re
import time

import cv2
import numpy as np
from PIL import Image

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"Robot({self.position}, {self.velocity})"

    def __repr__(self):
        return self.__str__()

    def move(self, width, height):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        if self.position.x < 0:
            self.position.x = width + self.position.x
        elif self.position.x >= width:
            self.position.x = self.position.x - width

        if self.position.y < 0:
            self.position.y = height + self.position.y
        elif self.position.y >= height:
            self.position.y = self.position.y - height

class Space:
    def __init__(self, width, height, robots):
        self.width = width
        self.height = height
        self.robots = robots

    def __str__(self):
        return f"Space({self.width}, {self.height}, {self.robots})"

    def __repr__(self):
        return self.__str__()

    def move(self):
        for robot in self.robots:
            robot.move(self.width, self.height)

    def print(self, quadrants=False):
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for robot in self.robots:
            grid[robot.position.y][robot.position.x] += 1

        grid = [[str(x) if x > 0 else "." for x in y] for y in grid]

        if quadrants:
            x_middle = self.width // 2
            y_middle = self.height // 2
            for y in range(self.height):
                for x in range(self.width):
                    if x == x_middle or y == y_middle:
                        grid[y][x] = " "

        print("\n".join(["".join(x) for x in grid]))
        print()

    def calculate_safety(self):
        x_middle = self.width // 2
        y_middle = self.height // 2
        safety = {"q1": 0, "q2": 0, "q3": 0, "q4": 0}
        for robot in self.robots:
            if   robot.position.x < x_middle and robot.position.y < y_middle:
                safety["q1"] += 1
            elif robot.position.x > x_middle and robot.position.y < y_middle:
                safety["q2"] += 1
            elif robot.position.x < x_middle and robot.position.y > y_middle:
                safety["q3"] += 1
            elif robot.position.x > x_middle and robot.position.y > y_middle:
                safety["q4"] += 1
        return safety["q1"] * safety["q2"] * safety["q3"] * safety["q4"]

    def draw(self, scale_factor, wait=1):
        image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for robot in self.robots:
            image[robot.position.y, robot.position.x] = (0, 0, 255)
        scaled_image = cv2.resize(image, (self.width * scale_factor, self.height * scale_factor), interpolation=cv2.INTER_NEAREST)
        cv2.imshow(f"Robots", scaled_image)
        cv2.waitKey(wait)

def part1(input_lines, width, height):
    robots = []
    for line in input_lines:
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()
        robots.append(Robot(Position(int(match[0]), int(match[1])), Velocity(int(match[2]), int(match[3]))))

    space = Space(width, height, robots)
    print(space)

    space.print()
    for ii in range(100):
        space.move()
    space.print(True)
    print(space.calculate_safety())

def part2(input_lines, width, height):
    robots = []
    for line in input_lines:
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()
        robots.append(Robot(Position(int(match[0]), int(match[1])), Velocity(int(match[2]), int(match[3]))))

    space = Space(width, height, robots)
    print(space)

    print(0)
    # space.draw(10)
    for ii in range(7500):
        space.move()
        print(ii + 1)
        if ii + 1 >= 7490:
            space.draw(10, 0)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        width, height = 11, 7
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        width, height = 101,103
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        part1(inputLines, width, height)
    elif part == 2:
        part2(inputLines, width, height)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
