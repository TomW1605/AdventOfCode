import time

from enum import Enum
from pydantic import BaseModel, computed_field

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
    Direction: Direction

    def move(self, grid):
        next_step = [self.X, self.Y]
        match self.Direction:
            case Direction.UP:
                next_step[1] += 1
            case Direction.DOWN:
                next_step[1] -= 1
            case Direction.LEFT:
                next_step[0] -= 1
            case Direction.RIGHT:
                next_step[0] += 1
        if (next_step[0] >= len(grid) or next_step[1] >= len(grid[0]) or
            grid[next_step[1]][next_step[0]].is_obstacle):
            self.Direction = self.Direction.rotate_right()
        else:
            grid[self.Y][self.X].type = "X"
            self.X = next_step[0]
            self.Y = next_step[1]

class MapPoint(BaseModel):
    type: str

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

class Map(BaseModel):
    grid: list[list[MapPoint]]

    def __str__(self):
        return "\n".join(["".join([point.type for point in line]) for line in self.grid])

def part1(input_lines):
    map = Map(grid=[[MapPoint(type=space) for space in line] for line in input_lines])
    grid = map.grid
    guard = None
    for line in grid:
        for point in line:
            if point.is_guard:
                guard = Guard(X=line.index(point), Y=grid.index(line), Direction=Direction(point.type))
                point.type = "."
                break
        if guard:
            break

    while not grid[guard.Y][guard.X].visited:
        guard.move(grid)
    print(map)

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
