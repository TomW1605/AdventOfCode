import math

from readFile import readFile

def printGrid(grid: list[list[int]]):
    height = len(grid)
    for row in range(1, height-1):
        print("\t".join([str(num) for num in grid[row][1:-1]]))
    print("")

def flashOctopus(grid: list[list[int]], row: int, col: int) -> list[list[int]]:
    if grid[row][col] >= 10:
        grid[row][col] = -1
        searchList = [
            [row-1, col-1], [row-1, col], [row-1, col+1],
            [row, col-1], [row, col], [row, col+1],
            [row+1, col-1], [row+1, col], [row+1, col+1]
        ]

        for searchRow, searchCol in searchList:
            if -1 < grid[searchRow][searchCol] < math.inf:
                grid[searchRow][searchCol] += 1
                if grid[searchRow][searchCol] >= 10:
                    grid = flashOctopus(grid, searchRow, searchCol)
            #printGrid(grid)

    return grid

def part1(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    grid = [[math.inf]*(width+2)]+[[math.inf]+[int(point) for point in list(line)]+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]

    steps = 100
    flashes = 0

    print(0)
    printGrid(grid)

    for step in range(1, steps+1):
        print(step)
        printGrid(grid)

        # increase all by 1
        for row in range(1, height+1):
            for col in range(1, width+1):
                grid[row][col] += 1
        printGrid(grid)

        for row in range(1, height+1):
            for col in range(1, width+1):
                grid = flashOctopus(grid, row, col)
        printGrid(grid)

        #set all flashed to 0
        for row in range(1, height+1):
            #print(grid[row])
            for col in range(1, width+1):
                if grid[row][col] == -1:
                    grid[row][col] = 0
                    flashes += 1
        printGrid(grid)
    print(flashes)

def part2(input_lines):
    print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    grid = [[math.inf]*(width+2)]+[[math.inf]+[int(point) for point in list(line)]+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]
    targetGrid = [[math.inf]*(width+2)]+[[math.inf]+[0]*width+[math.inf] for line in input_lines]+[[math.inf]*(width+2)]

    step = 0

    print(0)
    printGrid(grid)

    while grid != targetGrid:
        step += 1
        print(step)
        #printGrid(grid)

        # increase all by 1
        for row in range(1, height+1):
            for col in range(1, width+1):
                grid[row][col] += 1
        #printGrid(grid)

        for row in range(1, height+1):
            for col in range(1, width+1):
                grid = flashOctopus(grid, row, col)
        #printGrid(grid)

        # set all flashed to 0
        for row in range(1, height+1):
            # print(grid[row])
            for col in range(1, width+1):
                if grid[row][col] == -1:
                    grid[row][col] = 0
        printGrid(grid)
    print(step)

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
