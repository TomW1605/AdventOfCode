import math
from dataclasses import dataclass, field
from functools import total_ordering

from readFile import readFile

class Cave:
    pass

@dataclass
@total_ordering
class Cave:
    name: str
    max: int
    links: list[Cave]
    visited: int = 0

    def _is_valid_operand(self, other):
        return hasattr(other, "name") or type(other) == str

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        if type(other) == str:
            return self.name == other
        return self.name == other.name

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        if type(other) == str:
            return self.name < other
        return self.name < other.name

def printAllPaths(start: Cave, end: Cave, path, paths: set[tuple[str]], toPrint: bool = True) -> set[tuple[str]]:
    # Mark the current node as visited and store in path
    start.visited += 1
    path.append(start.name)

    # If current vertex is same as destination, then print
    # current path[]
    if start == end:
        if toPrint:
            print(",".join(path))
        paths.add(tuple(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for cave in start.links:
            if cave.visited < cave.max:
                paths = printAllPaths(cave, end, path, paths, toPrint)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    start.visited -= 1
    return paths

def part1(input_lines):
    print(input_lines)

    caves = {}
    for line in input_lines:
        cave1, cave2 = line.split("-")

        if cave1.lower() in caves:
            cave1 = caves[cave1.lower()]
        else:
            cave1 = Cave(cave1.lower(), 1 if cave1.islower() else math.inf, [])
            caves[cave1.name] = cave1

        if cave2.lower() in caves:
            cave2 = caves[cave2.lower()]
        else:
            cave2 = Cave(cave2.lower(), 1 if cave2.islower() else math.inf, [])
            caves[cave2.name] = cave2

        cave1.links.append(cave2)
        cave2.links.append(cave1)

    #print(caves)

    print(len(printAllPaths(caves["start"], caves["end"], [], set())))


def part2(input_lines):
    print(input_lines)

    caves = []
    for line in input_lines:
        cave1, cave2 = line.split("-")

        if cave1 in caves:
            cave1 = caves[caves.index(cave1)]
        else:
            cave1 = Cave(cave1, 1 if cave1.islower() else math.inf, [])
            caves.append(cave1)

        if cave2 in caves:
            cave2 = caves[caves.index(cave2)]
        else:
            cave2 = Cave(cave2, 1 if cave2.islower() else math.inf, [])
            caves.append(cave2)

        cave1.links.append(cave2)
        cave2.links.append(cave1)

    print(caves)
    paths = set()
    for cave in caves:
        if cave.max == 1 and cave not in ["start", "end"]:
            cave.max = 2
            paths = printAllPaths(caves[caves.index("start")], caves[caves.index("end")], [], paths)
            cave.max = 1
    print(len(paths))

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

