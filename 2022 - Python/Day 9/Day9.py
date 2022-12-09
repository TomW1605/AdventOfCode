from typing import List

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


def print_grid(knots: List[Knot], max_point, min_point):
    for yy in range(max_point[1]+1, min_point[1], -1):
        for xx in range(min_point[0], max_point[0]+1):
            #print([xx, yy])
            if Knot(xx, yy-1) in knots:
                print(knots[knots.index(Knot(xx, yy-1))].name, end="")
            elif [xx, yy-1] == [0, 0]:
                print("s", end="")
            else:
                print(".", end="")
        print()


def part1(input_lines):
    print(input_lines)
    visited = {Knot(0, 0)}
    knots = [Knot(0, 0, "H"), Knot(0, 0, "T")]
    max_point = [0, 0]
    min_point = [0, 0]

    for line in input_lines:
        direction, distance = line.split()
        for ii in range(int(distance)):
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

            #print(knots[0], knots[1])
            #print_grid(knots, max_point, min_point)

            if not adjacent(knots[0], knots[1]):
                print("not adjacent")

                if knots[1].x > knots[0].x:
                    knots[1].x -= 1

                if knots[1].y > knots[0].y:
                    knots[1].y -= 1

                if knots[1].x < knots[0].x:
                    knots[1].x += 1

                if knots[1].y < knots[0].y:
                    knots[1].y += 1

                #print_grid(knots, max_point, min_point)

                visited.add(knots[1])
            #print(visited)
            #print()

    print(len(visited))


def part2(input_lines):
    print(input_lines)
    visited = {Knot(0, 0)}
    knots = [Knot(0, 0, "H"), Knot(0, 0, "1"), Knot(0, 0, "2"), Knot(0, 0, "3"), Knot(0, 0, "4"),
             Knot(0, 0, "5"), Knot(0, 0, "6"), Knot(0, 0, "7"), Knot(0, 0, "8"), Knot(0, 0, "9")]
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

            #print(knots)
            #print_grid(knots, max_point, min_point)

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
                        visited.add(knots[ii])
        #print_grid(knots, max_point, min_point)
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
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

