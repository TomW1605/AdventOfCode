import time
from collections import defaultdict
from enum import Enum
from functools import cached_property

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self.value[0]

    @property
    def y(self):
        return self.value[1]

Directions = Direction

class Plant:
    def __init__(self, plant_type, x, y):
        self.type = plant_type
        self.x = x
        self.y = y
        self.in_region = False

    def __str__(self):
        return f"Plant({self.type}, ({self.x}, {self.y}), {self.in_region})"

    def __repr__(self):
        return self.__str__()

    def neighbors(self, grid):
        neighbors = []
        for direction in Directions:
            x = self.x + direction.x
            y = self.y + direction.y
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                neighbors.append((grid[y][x], direction))
            else:
                neighbors.append((None, direction))
        return neighbors

class Region:
    def __init__(self, plant_type):
        self.type = plant_type
        self.plants = []
        self.perimeter = 0
        self._vertical_sides = defaultdict(list)
        self._horizontal_sides = defaultdict(list)

    def __str__(self):
        return f"Region({self.type})"

    def __repr__(self):
        return self.__str__()

    def generate(self, start_point: tuple[int, int], grid: list[list[Plant]]):
        queue = [start_point]
        while queue:
            point = queue.pop(0)
            plant = grid[point[1]][point[0]]
            if plant.in_region:
                continue
            plant.in_region = True
            self.plants.append(plant)
            for neighbor, direction in plant.neighbors(grid):
                if neighbor and neighbor.type == self.type:
                    queue.append((neighbor.x, neighbor.y))
                else:
                    if direction in (Directions.UP, Directions.DOWN):
                        self._horizontal_sides[(plant.y + direction.y, direction)].append(plant.x + direction.x)
                    elif direction in (Directions.LEFT, Directions.RIGHT):
                        self._vertical_sides[(plant.x + direction.x, direction)].append(plant.y + direction.y)
                    self.perimeter += 1
        return self.type

    @cached_property
    def area(self):
        return len(self.plants)

    @cached_property
    def sides(self):
        sides = 0
        for plane in self._horizontal_sides.values():
            plane.sort()
            for ii in range(len(plane) - 1):
                if plane[ii] + 1 != plane[ii + 1]:
                    sides += 1
            sides += 1

        for plane in self._vertical_sides.values():
            plane.sort()
            for ii in range(len(plane) - 1):
                if plane[ii] + 1 != plane[ii + 1]:
                    sides += 1
            sides += 1

        return sides

def print_grid(grid):
    for row in grid:
        for plant in row:
            if plant.in_region:
                print(plant.type.lower(), end="")
            else:
                print(plant.type, end="")
        print()

def part1(input_lines):
    grid = [[Plant(point, x, y) for x, point in enumerate(line)] for y, line in enumerate(input_lines)]
    regions = []
    for row in grid:
        for plant in row:
            if plant.in_region:
                continue
            new_region = Region(plant.type)
            new_region.generate((plant.x, plant.y), grid)
            regions.append(new_region)

    total = 0
    for region in regions:
        total += region.area * region.perimeter
    print_grid(grid)
    print(total)

def part2(input_lines):
    grid = [[Plant(point, x, y) for x, point in enumerate(line)] for y, line in enumerate(input_lines)]
    regions = []
    for row in grid:
        for plant in row:
            if plant.in_region:
                continue
            new_region = Region(plant.type)
            new_region.generate((plant.x, plant.y), grid)
            regions.append(new_region)

    total = 0
    for region in regions:
        # print(f"A region of {region.type} plants with price {region.area} * {region.sides} = {region.area * region.sides}.")
        total += region.area * region.sides
    print_grid(grid)
    print(total)

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
