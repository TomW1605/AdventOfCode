import re
import time

import sympy as sym
from sympy.core.numbers import Integer as SympyInteger

class Coordinate:
    def __init__(self, point: tuple[int, int]):
        self.x = point[0]
        self.y = point[1]

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate((self.x + other.x, self.y + other.y))
        elif isinstance(other, int):
            return Coordinate((self.x + other, self.y + other))
        return NotImplemented

class Machine:
    def __init__(self, button_a: Coordinate, button_b: Coordinate, prize: Coordinate):
        self.buttonA = button_a
        self.buttonB = button_b
        self.prize = prize

    def __str__(self):
        return f"Machine({self.buttonA}, {self.buttonB}, {self.prize})"

    def __repr__(self):
        return self.__str__()

    def solve(self):
        a, b = sym.symbols("a, b")
        eq1 = sym.Eq(a * self.buttonA.x + b * self.buttonB.x, self.prize.x)
        eq2 = sym.Eq(a * self.buttonA.y + b * self.buttonB.y, self.prize.y)
        solution = sym.solve((eq1, eq2), (a, b), rational=False)
        if solution and isinstance(solution[a], SympyInteger) and isinstance(solution[b], SympyInteger):
            return solution[a]*3 + solution[b]
        return 0

def part1(input_lines):
    machines = []
    for machine_str in input_lines.split("\n\n"):
        button_a_str, button_b_str, prize_str = machine_str.split("\n")
        button_a = Coordinate(tuple(map(int, re.findall(r"\d+", button_a_str))))
        button_b = Coordinate(tuple(map(int, re.findall(r"\d+", button_b_str))))
        prize = Coordinate(tuple(map(int, re.findall(r"\d+", prize_str))))
        machine = Machine(button_a, button_b, prize)
        machines.append(machine)

    print(sum([machine.solve() for machine in machines]))

def part2(input_lines):
    machines = []
    for machine_str in input_lines.split("\n\n"):
        button_a_str, button_b_str, prize_str = machine_str.split("\n")
        button_a = Coordinate(tuple(map(int, re.findall(r"\d+", button_a_str))))
        button_b = Coordinate(tuple(map(int, re.findall(r"\d+", button_b_str))))
        prize = Coordinate(tuple(map(int, re.findall(r"\d+", prize_str))))
        prize += 10000000000000
        machine = Machine(button_a, button_b, prize)
        machines.append(machine)

    print(sum([machine.solve() for machine in machines]))

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read()#.splitlines()
    else:
        inputLines = open("input.txt", "r").read()#.splitlines()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
