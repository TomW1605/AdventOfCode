import numpy as np

from readFile import readFile


def part1(input_lines):
    print(input_lines)
    trees = np.array([[int(tree) for tree in row] for row in input_lines])

    visible = 0
    visible += trees.shape[0]*2 + (trees.shape[1]-2)*2

    for yy in range(1, trees.shape[0]-1):
        for xx in range(1, trees.shape[1]-1):
            print(trees.item((yy, xx)), end='\t')

            surrounding_trees = [max(trees[:yy, xx]), max(trees[yy+1:, xx]), max(trees[yy, :xx]), max(trees[yy, xx+1:])]
            print(surrounding_trees)

            for tree in surrounding_trees:
                if tree < trees[yy, xx]:
                    visible += 1
                    break

    print(visible)


def part2(input_lines):
    print(input_lines)
    trees = np.array([[int(tree) for tree in row] for row in input_lines])

    max_score = 0

    for yy in range(1, trees.shape[0]-1):
        for xx in range(1, trees.shape[1]-1):
            print(trees.item((yy, xx)), end='\t')

            surrounding_trees = [list(np.flip(trees[:yy, xx])), list(trees[yy+1:, xx]), list(np.flip(trees[yy, :xx])), list(trees[yy, xx+1:])]
            print(surrounding_trees)

            score = 1
            for sight_line in surrounding_trees:
                ii = 0
                for tree in sight_line:
                    ii += 1
                    if tree >= trees[yy, xx]:
                        break

                score *= ii

            if score > max_score:
                max_score = score

    print(max_score)

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

