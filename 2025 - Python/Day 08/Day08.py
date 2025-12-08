import itertools
import math
import time


class Node:
    circuit = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Node({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

    def distance(self, other):
        if isinstance(other, Node):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
        return None


class Circuit:
    def __init__(self, nodes):
        self.nodes = nodes
        for node in nodes:
            node.circuit = self

    def __str__(self):
        return f"Circuit({self.size}, {self.nodes})"

    def __repr__(self):
        return self.__str__()

    @property
    def size(self):
        return len(self.nodes)

    def merge(self, other):
        if isinstance(other, Circuit):
            return Circuit(self.nodes + other.nodes)
        return self


def part1(input_lines, iterations):
    print(input_lines)

    nodes = [Node(x, y, z) for x, y, z in (map(int, line.split(',')) for line in input_lines)]
    print(nodes)

    circuits = [Circuit([node]) for node in nodes]
    print(circuits)

    distances = [(pair[0].distance(pair[1]), pair) for pair in itertools.combinations(nodes, 2)]
    distances.sort()
    print(distances)

    for ii in range(iterations):
        distance, (node1, node2) = distances[ii]
        if node1.circuit == node2.circuit:
            continue

        circuits.remove(node1.circuit)
        circuits.remove(node2.circuit)
        circuits.append(node1.circuit.merge(node2.circuit))

    print(circuits)

    circuits.sort(key=lambda x: x.size, reverse=True)

    print(circuits[0].size * circuits[1].size * circuits[2].size)

def part2(input_lines):
    print(input_lines)

    nodes = [Node(x, y, z) for x, y, z in (map(int, line.split(',')) for line in input_lines)]
    print(nodes)

    circuits = [Circuit([node]) for node in nodes]
    print(circuits)

    distances = [(pair[0].distance(pair[1]), pair) for pair in itertools.combinations(nodes, 2)]
    distances.sort()
    print(distances)

    ii = 0
    while len(circuits) > 1:
        distance, (node1, node2) = distances[ii]
        if node1.circuit == node2.circuit:
            ii += 1
            continue

        circuits.remove(node1.circuit)
        circuits.remove(node2.circuit)
        circuits.append(node1.circuit.merge(node2.circuit))
        ii += 1

    print(node1.x * node2.x)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        iterations = 10 if test else 1000
        part1(inputLines, iterations)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
