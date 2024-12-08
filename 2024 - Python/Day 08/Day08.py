import itertools
import math
import time
from itertools import count

class Antenna:
    def __init__(self, x, y, freq):
        self.x = x
        self.y = y
        self.freq = freq

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    @property
    def position(self):
        return (self.x, self.y)

class Space:
    def __init__(self, contents):
        self.contents = contents

    # @property
    # def contents(self):
    #     return self._contents
    #
    # @contents.setter
    # def contents(self, value):
    #     if self._contents == ".":
    #         self._contents = value

    def __str__(self):
        if isinstance(self.contents, Antenna):
            return self.contents.freq
        else:
            return self.contents

    def __repr__(self):
        return self.__str__()

def part1(input_lines):
    grid = []
    antennas = {}
    for yy in range(len(input_lines)):
        row = []
        for xx in range(len(input_lines[yy])):
            antenna = "."
            if input_lines[yy][xx] != '.':
                antenna = Antenna(xx, yy, input_lines[yy][xx])
                if antenna.freq not in antennas:
                    antennas[antenna.freq] = []
                antennas[antenna.freq].append(antenna)
            row.append(Space(input_lines[yy][xx]))
        grid.append(row)

    for freq in antennas:
        print(f"Frequency: {freq}")
        for antenna_pair in itertools.combinations(antennas[freq], 2):
            x_dist = abs(antenna_pair[0].x - antenna_pair[1].x)
            y_dist = abs(antenna_pair[0].y - antenna_pair[1].y)
            point_1 = None
            point_2 = None
            if antenna_pair[0].x > antenna_pair[1].x and antenna_pair[0].y > antenna_pair[1].y:
                point_1 = (antenna_pair[0].x + x_dist, antenna_pair[0].y + y_dist)
                point_2 = (antenna_pair[1].x - x_dist, antenna_pair[1].y - y_dist)
            elif antenna_pair[0].x > antenna_pair[1].x and antenna_pair[0].y < antenna_pair[1].y:
                point_1 = (antenna_pair[0].x + x_dist, antenna_pair[0].y - y_dist)
                point_2 = (antenna_pair[1].x - x_dist, antenna_pair[1].y + y_dist)
            elif antenna_pair[0].x < antenna_pair[1].x and antenna_pair[0].y > antenna_pair[1].y:
                point_1 = (antenna_pair[0].x - x_dist, antenna_pair[0].y + y_dist)
                point_2 = (antenna_pair[1].x + x_dist, antenna_pair[1].y - y_dist)
            elif antenna_pair[0].x < antenna_pair[1].x and antenna_pair[0].y < antenna_pair[1].y:
                point_1 = (antenna_pair[0].x - x_dist, antenna_pair[0].y - y_dist)
                point_2 = (antenna_pair[1].x + x_dist, antenna_pair[1].y + y_dist)
            if 0 <= point_1[0] < len(grid[0]) and 0 <= point_1[1] < len(grid):
                grid[point_1[1]][point_1[0]].contents = "#"
            if 0 <= point_2[0] < len(grid[0]) and 0 <= point_2[1] < len(grid):
                grid[point_2[1]][point_2[0]].contents = "#"
            # print(antenna_pair, distance)
    print("\n".join(["".join([str(space) for space in row]) for row in grid]))
    print(sum([1 for row in grid for space in row if space.contents == "#"]))

def calc_antinodes(grid, antenna, x_dist, y_dist):
    ii = 0
    point = antenna.position
    while 0 <= point[1] + y_dist*ii < len(grid[0]) and 0 <= point[0] + x_dist*ii < len(grid):
        grid[point[1] + y_dist*ii][point[0] + x_dist*ii].contents = "#"
        ii += 1

def part2(input_lines):
    grid = []
    antennas = {}
    for yy in range(len(input_lines)):
        row = []
        for xx in range(len(input_lines[yy])):
            antenna = "."
            if input_lines[yy][xx] != '.':
                antenna = Antenna(xx, yy, input_lines[yy][xx])
                if antenna.freq not in antennas:
                    antennas[antenna.freq] = []
                antennas[antenna.freq].append(antenna)
            row.append(Space(input_lines[yy][xx]))
        grid.append(row)

    for freq in antennas:
        print(f"Frequency: {freq}")
        for antenna_pair in itertools.combinations(antennas[freq], 2):
            x_dist = abs(antenna_pair[0].x - antenna_pair[1].x)
            y_dist = abs(antenna_pair[0].y - antenna_pair[1].y)
            if antenna_pair[0].x > antenna_pair[1].x and antenna_pair[0].y > antenna_pair[1].y:
                calc_antinodes(grid, antenna_pair[0], +x_dist, +y_dist)
                calc_antinodes(grid, antenna_pair[1], -x_dist, -y_dist)
            elif antenna_pair[0].x > antenna_pair[1].x and antenna_pair[0].y < antenna_pair[1].y:
                calc_antinodes(grid, antenna_pair[0], +x_dist, -y_dist)
                calc_antinodes(grid, antenna_pair[1], -x_dist, +y_dist)
            elif antenna_pair[0].x < antenna_pair[1].x and antenna_pair[0].y > antenna_pair[1].y:
                calc_antinodes(grid, antenna_pair[0], -x_dist, +y_dist)
                calc_antinodes(grid, antenna_pair[1], +x_dist, -y_dist)
            elif antenna_pair[0].x < antenna_pair[1].x and antenna_pair[0].y < antenna_pair[1].y:
                calc_antinodes(grid, antenna_pair[0], -x_dist, -y_dist)
                calc_antinodes(grid, antenna_pair[1], +x_dist, +y_dist)
            # print(antenna_pair, distance)
    print("\n".join(["".join([str(space) for space in row]) for row in grid]))
    print(sum([1 for row in grid for space in row if space.contents == "#"]))

if __name__ == '__main__':
    test = 0
    part = 2

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
