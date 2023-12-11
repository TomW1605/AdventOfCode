import math
import time

# from termcolor import colored

#from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

def print_universe(universe, path=[], inside=[]):
    universe_string = ''
    for row in range(len(universe)):
        print(''.join(universe[row]))
        # for column in range(len(universe[row])):
        #     if universe[row][column] == "#":
        #         # universe_string += colored('#', on_color='on_red')
        #         universe_string += '#'
        #     # elif universe[row][column] in range(10):
        #     #     # universe_string += colored(universe[row][column], on_color='on_red')
        #     #     universe_string += universe[row][column]
        #     # elif (row, column) in path:
        #     #     universe_string += colored(pipe_map[row][column], 'red', on_color='on_grey')
        #     # elif (row, column) in inside:
        #     #     universe_string += colored(pipe_map[row][column], on_color='on_green')
        #     else:
        #         # universe_string += colored('.', on_color='on_grey')
        #         universe_string += '.'
        # universe_string += '\n'
    # print('\n'.join(map))
    print(universe_string)

def part1(input_lines):
    # print_universe(input_lines)

    universe = []
    for line in input_lines:
        if '#' in line:
            universe.append(list(line))
        else:
            universe.append(list(line))
            universe.append(list(line))

    # print_universe(universe)

    temp_universe = []
    universe = [list(x) for x in zip(*universe)]
    print_universe(universe)
    for line in universe:
        if '#' in line:
            temp_universe.append(line)
        else:
            temp_universe.append(line)
            temp_universe.append(line)

    #this is completely unnecessary since it dosnt impact the distance calculation
    universe = [list(x) for x in zip(*temp_universe)]
    print_universe(universe)

    galaxies = []
    for row in range(len(universe)):
        for column in range(len(universe[row])):
            if universe[row][column] == "#":
                # universe[row][column] = len(galaxies)
                galaxies.append((row, column))

    print_universe(universe)

    print(galaxies)
    # print((galaxies[8][0] - galaxies[4][0]) + (galaxies[8][1] - galaxies[4][1]))
    # print((galaxies[6][0] - galaxies[1][0]) + (galaxies[6][1] - galaxies[1][1]))

    new_pairs = [[(galaxies[start], galaxies[end]) for end in range(start+1, len(galaxies))] for start in range(len(galaxies))]
    pairs = []
    for pair in new_pairs:
        pairs += pair
    # print(len(pairs))

    total = 0
    for pair in pairs:
        total += abs(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]))
    print(total)

def part2(input_lines):
    # print_universe(input_lines)

    universe = []
    print("expansion 1 start")
    for line in input_lines:
        if '#' in line:
            universe.append(list(line))
        else:
            # universe.append(list(line))
            for ii in range(1000000):
                universe.append(list(line))

    print("expansion 1 complete")
    # print_universe(universe)
    # for row in range(len(universe)):
    #     print(''.join(universe[row]))

    temp_universe = []
    print("rotation 1 start")
    universe = [list(x) for x in zip(*universe)]
    print("rotation 1 complete")
    # print_universe(universe)
    # for row in range(len(universe)):
    #     print(''.join(universe[row]))
    print("expansion 2 start")
    for line in universe:
        if '#' in line:
            temp_universe.append(line)
        else:
            # temp_universe.append(line)
            for ii in range(1000000):
                temp_universe.append(list(line))
    print("expansion 2 complete")

    #this is completely unnecessary since it dosnt impact the distance calculation
    print("rotation 2 start")
    universe = [list(x) for x in zip(*temp_universe)]
    print("rotation 2 complete")
    # print_universe(universe)

    galaxies = []
    for row in range(len(universe)):
        for column in range(len(universe[row])):
            if universe[row][column] == "#":
                # universe[row][column] = len(galaxies)
                galaxies.append((row, column))

    # print_universe(universe)

    print(galaxies)
    # print((galaxies[8][0] - galaxies[4][0]) + (galaxies[8][1] - galaxies[4][1]))
    # print((galaxies[6][0] - galaxies[1][0]) + (galaxies[6][1] - galaxies[1][1]))

    new_pairs = [[(galaxies[start], galaxies[end]) for end in range(start+1, len(galaxies))] for start in range(len(galaxies))]
    pairs = []
    for pair in new_pairs:
        pairs += pair
    # print(len(pairs))

    total = 0
    for pair in pairs:
        total += abs(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]))
    print(total)


if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")