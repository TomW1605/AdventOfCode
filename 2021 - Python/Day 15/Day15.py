import math
from dataclasses import dataclass

from readFile import readFile

@dataclass
class Position:
    row: int
    col: int
    value: float = 0
    visited: bool = False

    def _is_valid_operand(self, other):
        return hasattr(other, "row") and hasattr(other, "col") and hasattr(other, "value")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.col == other.col and self.row == other.row
    
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.value < other.value

def findPath(grid: list[list[Position]], pos, lastPos, target, path: list[Position], paths: list[tuple[Position]]):
    row = pos.row
    col = pos.col

    path.append(pos)
    pos.visited = True

    if pos == target:
        #if toPrint:
        print(",".join([str(cord) for cord in path]))
        paths.append(tuple(path))
    else:
        searchList = [
                            [row - 1, col],
            [row, col - 1],                 [row, col + 1],
                            [row + 1, col]
        ]

        adjacentSpaces = [grid[searchRow][searchCol] for searchRow, searchCol in searchList if not grid[searchRow][searchCol].visited and grid[searchRow][searchCol].value < math.inf]
        print(adjacentSpaces)
        minRisk = min(adjacentSpaces).value
        #print(minRisk)
        nextSpaces = [position for position in adjacentSpaces if position.value == minRisk]
        #print(nextSpaces)
        for space in nextSpaces:
            paths = findPath(grid, space, pos, target, path, paths)

    path.pop()
    pos.visited = False
    return paths

def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    intGrid = [[math.inf] * (width + 2)] + [[math.inf] + [int(point) for point in list(line)] + [math.inf] for line in input_lines] + [[math.inf] * (width + 2)]
    grid = []
    for ii in range(len(intGrid[0])):
        row = []
        for jj in range(len(intGrid)):
            row.append(Position(jj, ii, intGrid[jj][ii]))
        grid.append(row)
    print(grid)

    pos = Position(1, 1)
    target = Position(width, height)
    findPath(grid, pos, Position(0, 0), target, [], [])


def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 1
    part = 1

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

