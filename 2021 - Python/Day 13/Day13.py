from enum import Enum
import matplotlib.pyplot as plt

from readFile import readFile

class FoldAxis(Enum):
    x = 0
    y = 1

def part1(input_lines):
    print(input_lines)

    fold = False
    dots = []
    folds = []
    for line in input_lines:
        if line == "":
            fold = True
            continue

        if not fold:
            dots.append([int(cord) for cord in line.split(",")])
        else:
            foldAxis, foldLine = line.split(" ")[2].split("=")
            if foldAxis == "x":
                foldAxis = FoldAxis.x
            elif foldAxis == "y":
                foldAxis = FoldAxis.y
            folds.append([foldAxis, int(foldLine)])

    print(len(set([tuple(dot) for dot in dots])))
    #print(folds)

    foldAxis, foldLine = folds[0]
    for dot in dots:
        if dot[foldAxis.value] > foldLine:
            dot[foldAxis.value] = foldLine - (dot[foldAxis.value] - foldLine)

    print(len(set([tuple(dot) for dot in dots])))

def part2(input_lines):
    print(input_lines)

    fold = False
    dots = []
    folds = []
    for line in input_lines:
        if line == "":
            fold = True
            continue

        if not fold:
            dots.append([int(cord) for cord in line.split(",")])
        else:
            foldAxis, foldLine = line.split(" ")[2].split("=")
            if foldAxis == "x":
                foldAxis = FoldAxis.x
            elif foldAxis == "y":
                foldAxis = FoldAxis.y
            folds.append([foldAxis, int(foldLine)])

    for foldAxis, foldLine in folds:
        for dot in dots:
            if dot[foldAxis.value] > foldLine:
                dot[foldAxis.value] = foldLine - (dot[foldAxis.value] - foldLine)

    print(set([tuple(dot) for dot in dots]))
    plt.figure(figsize=(5, 1))
    plt.scatter(*zip(*set([(dot[0], -dot[1]) for dot in dots])))
    plt.show()

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

