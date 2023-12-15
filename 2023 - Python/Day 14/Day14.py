import copy
import time

from tqdm import tqdm

#from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output


def part1(input_lines):
    print(input_lines)

    platform = [list(line) for line in input_lines]

    print('\n'.join([''.join(row) for row in platform]))
    print()

    # for row in range(1, len(platform)):
    #     for column in range(len(platform[row])):
    #         if platform[row][column] == 'O':
    #             ii = row
    #             while ii > 0:
    #                 if platform[ii-1][column] == '.':
    #                     platform[ii][column] = '.'
    #                     platform[ii-1][column] = 'O'
    #                     ii -= 1
    #                 else:
    #                     break

    for row in range(len(platform)):
        for column in range(len(platform[row])-2, -1, -1):
            if platform[row][column] == 'O':
                ii = column
                while ii < len(platform[row]) - 1:
                    if platform[row][ii+1] == '.':
                        platform[row][ii] = '.'
                        platform[row][ii+1] = 'O'
                        ii += 1
                    else:
                        break

    print('\n'.join([''.join(row) for row in platform]))

    total = 0

    for row in range(len(platform)):
        total += platform[row].count("O") * (len(platform) - row)

    print(total)
    print(109939)
    print("00:00:00.033")

def part2(input_lines):
    # print(input_lines)

    platform = [list(line) for line in input_lines]

    # print('\n'.join([''.join(row) for row in platform]))
    # print()

    all_platforms = []
    for jj in tqdm(range(1000)):#147695
    # for jj in range(1000):  #147695
        platforms = []
        platforms.append(copy.deepcopy(platform))
        for row in range(1, len(platform)):
            for column in range(len(platform[row])):
                if platform[row][column] == 'O':
                    ii = row
                    while ii > 0:
                        if platform[ii-1][column] == '.':
                            platform[ii][column] = '.'
                            platform[ii-1][column] = 'O'
                            ii -= 1
                        else:
                            break
        platforms.append(copy.deepcopy(platform))

        for row in range(len(platform)):
            for column in range(1, len(platform[row])):
                if platform[row][column] == 'O':
                    ii = column
                    while ii > 0:
                        if platform[row][ii-1] == '.':
                            platform[row][ii] = '.'
                            platform[row][ii-1] = 'O'
                            ii -= 1
                        else:
                            break
        platforms.append(copy.deepcopy(platform))

        for row in range(len(platform)-2, -1, -1):
            for column in range(len(platform[row])):
                if platform[row][column] == 'O':
                    ii = row
                    while ii < len(platform)-1:
                        if platform[ii+1][column] == '.':
                            platform[ii][column] = '.'
                            platform[ii+1][column] = 'O'
                            ii += 1
                        else:
                            break
        platforms.append(copy.deepcopy(platform))

        for row in range(len(platform)):
            for column in range(len(platform[row])-2, -1, -1):
                if platform[row][column] == 'O':
                    ii = column
                    while ii < len(platform[row])-1:
                        if platform[row][ii+1] == '.':
                            platform[row][ii] = '.'
                            platform[row][ii+1] = 'O'
                            ii += 1
                        else:
                            break
        platforms.append(copy.deepcopy(platform))

        # print('\n'.join([''.join(row) for row in platform]))
        # print()

        # for xx in range(len(platforms[0])):
        #     for platform in platforms:
        #         print(''.join(platform[xx]), end='   ')
        #     print()
        # print()

        # if platform in all_platforms:
        #     print(jj)
        #     break
        #
        # all_platforms.append(copy.deepcopy(platform))

    total = 0

    for row in range(len(platform)):
        total += platform[row].count("O")*(len(platform)-row)

    print(total)


if __name__ == '__main__':
    test = 1
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