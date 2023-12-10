import time
from termcolor import colored

# from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

def print_map(pipe_map, path=[], inside=[]):
    map_string = ''
    for row in range(len(pipe_map)):
        for column in range(len(pipe_map[row])):
            if pipe_map[row][column] == "S":
                map_string += colored(pipe_map[row][column], 'red', on_color='on_grey')
            elif (row, column) in path:
                map_string += colored(pipe_map[row][column], 'red', on_color='on_grey')
            elif (row, column) in inside:
                map_string += colored(pipe_map[row][column], on_color='on_green')
            else:
                map_string += colored(pipe_map[row][column], on_color='on_blue')
        map_string += '\n'
    # print('\n'.join(map))
    print(map_string)

def trace_path(pipe_map, point, path):
    # print_map(pipe_map, path)
    match pipe_map[point[0]][point[1]]:
        case 'S':
            if pipe_map[point[0]][point[1]-1] in ['─', '┌', '└'] and (point[0], point[1]-1) not in path:
                path.append((point[0], point[1]-1))
                path = trace_path(pipe_map, (point[0], point[1]-1), path)
            elif pipe_map[point[0]][point[1]+1] in ['─', '┐', '┘'] and (point[0], point[1]+1) not in path:
                path.append((point[0], point[1]+1))
                path = trace_path(pipe_map, (point[0], point[1]+1), path)
            elif pipe_map[point[0]-1][point[1]] in ['│', '┌', '┐'] and (point[0]-1, point[1]) not in path:
                path.append((point[0]-1, point[1]))
                path = trace_path(pipe_map, (point[0]-1, point[1]), path)
            elif pipe_map[point[0]+1][point[1]] in ['│', '└', '┘'] and (point[0]+1, point[1]) not in path:
                path.append((point[0]+1, point[1]))
                path = trace_path(pipe_map, (point[0]+1, point[1]), path)
        case '─':
            if (point[0], point[1]-1) not in path:
                path.append((point[0], point[1]-1))
                path = trace_path(pipe_map, (point[0], point[1]-1), path)
            elif (point[0], point[1]+1) not in path:
                path.append((point[0], point[1]+1))
                path = trace_path(pipe_map, (point[0], point[1]+1), path)
        case '│':
            if (point[0]-1, point[1]) not in path:
                path.append((point[0]-1, point[1]))
                path = trace_path(pipe_map, (point[0]-1, point[1]), path)
            elif (point[0]+1, point[1]) not in path:
                path.append((point[0]+1, point[1]))
                path = trace_path(pipe_map, (point[0]+1, point[1]), path)
        case '┌':
            if (point[0], point[1]+1) not in path:
                path.append((point[0], point[1]+1))
                path = trace_path(pipe_map, (point[0], point[1]+1), path)
            elif (point[0]+1, point[1]) not in path:
                path.append((point[0]+1, point[1]))
                path = trace_path(pipe_map, (point[0]+1, point[1]), path)
        case '┐':
            if (point[0], point[1]-1) not in path:
                path.append((point[0], point[1]-1))
                path = trace_path(pipe_map, (point[0], point[1]-1), path)
            elif (point[0]+1, point[1]) not in path:
                path.append((point[0]+1, point[1]))
                path = trace_path(pipe_map, (point[0]+1, point[1]), path)
        case '└':
            if (point[0]-1, point[1]) not in path:
                path.append((point[0]-1, point[1]))
                path = trace_path(pipe_map, (point[0]-1, point[1]), path)
            elif (point[0], point[1]+1) not in path:
                path.append((point[0], point[1]+1))
                path = trace_path(pipe_map, (point[0], point[1]+1), path)
        case '┘':
            if (point[0], point[1]-1) not in path:
                path.append((point[0], point[1]-1))
                path = trace_path(pipe_map, (point[0], point[1]-1), path)
            elif (point[0]-1, point[1]) not in path:
                path.append((point[0]-1, point[1]))
                path = trace_path(pipe_map, (point[0]-1, point[1]), path)
    return path

def part1(pipe_map):
    # print_map(pipe_map)

    path = []
    # {
    #     'left': [],
    #     'right': []
    # }

    start = (-1, -1)

    for ii in range(len(pipe_map)):
        for jj in range(len(pipe_map[ii])):
            if pipe_map[ii][jj] == 'S':
                start = (ii, jj)
                break
        if start != (-1, -1):
            break

    path.append(start)

    # trace_path(pipe_map, start, path)
    left = (-1, -1)
    right = (len(pipe_map), len(pipe_map[0]))
    point = start
    length = -1

    old_point = (-1, -1)
    while point != old_point:
        old_point = point
        length += 1
        match pipe_map[point[0]][point[1]]:
            case 'S':
                if pipe_map[point[0]][point[1]-1] in ['─', '┌', '└'] and (point[0], point[1]-1) not in path:
                    path.append((point[0], point[1]-1))
                    point = (point[0], point[1]-1)
                elif pipe_map[point[0]][point[1]+1] in ['─', '┐', '┘'] and (point[0], point[1]+1) not in path:
                    path.append((point[0], point[1]+1))
                    point = (point[0], point[1]+1)
                elif pipe_map[point[0]-1][point[1]] in ['│', '┌', '┐'] and (point[0]-1, point[1]) not in path:
                    path.append((point[0]-1, point[1]))
                    point = (point[0]-1, point[1])
                elif pipe_map[point[0]+1][point[1]] in ['│', '└', '┘'] and (point[0]+1, point[1]) not in path:
                    path.append((point[0]+1, point[1]))
                    point = (point[0]+1, point[1])
            case '─':
                if (point[0], point[1]-1) not in path:
                    path.append((point[0], point[1]-1))
                    point = (point[0], point[1]-1)
                elif (point[0], point[1]+1) not in path:
                    path.append((point[0], point[1]+1))
                    point = (point[0], point[1]+1)
            case '│':
                if (point[0]-1, point[1]) not in path:
                    path.append((point[0]-1, point[1]))
                    point = (point[0]-1, point[1])
                elif (point[0]+1, point[1]) not in path:
                    path.append((point[0]+1, point[1]))
                    point = (point[0]+1, point[1])
            case '┌':
                if (point[0], point[1]+1) not in path:
                    path.append((point[0], point[1]+1))
                    point = (point[0], point[1]+1)
                elif (point[0]+1, point[1]) not in path:
                    path.append((point[0]+1, point[1]))
                    point = (point[0]+1, point[1])
            case '┐':
                if (point[0], point[1]-1) not in path:
                    path.append((point[0], point[1]-1))
                    point = (point[0], point[1]-1)
                elif (point[0]+1, point[1]) not in path:
                    path.append((point[0]+1, point[1]))
                    point = (point[0]+1, point[1])
            case '└':
                if (point[0]-1, point[1]) not in path:
                    path.append((point[0]-1, point[1]))
                    point = (point[0]-1, point[1])
                elif (point[0], point[1]+1) not in path:
                    path.append((point[0], point[1]+1))
                    point = (point[0], point[1]+1)
            case '┘':
                if (point[0], point[1]-1) not in path:
                    path.append((point[0], point[1]-1))
                    point = (point[0], point[1]-1)
                elif (point[0]-1, point[1]) not in path:
                    path.append((point[0]-1, point[1]))
                    point = (point[0]-1, point[1])
        # print(length)

    # print_map(pipe_map, path)
    # print((length+1)/2)

    return path


def part2(pipe_map):
    path = part1(pipe_map)

    for row in range(1, len(pipe_map)-1):
        for column in range(1, len(pipe_map[row])-1):
            if (row, column) not in path:
                pipe_map[row][column] = ' '

    inside = []

    for row in range(1, len(pipe_map)-1):
        for column in range(1, len(pipe_map[row])-1):
            if (row, column) in path:
                continue
            ray = pipe_map[row][:column]
            crosses = ray.count('│') + int(((ray.count('┐') - ray.count('┌')) + (ray.count('└') - ray.count('┘')))/2)
            if crosses % 2 == 1:
                inside.append((row, column))

            # print(ray)

    print_map(pipe_map, path, inside)
    # print(len(inside))


if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    inputLines = ['.' * len(inputLines[0])] + inputLines + ['.' * len(inputLines[0])]

    for ii in range(len(inputLines)):
        inputLines[ii] = '.' + inputLines[ii] + '.'

    replacements = {
        '-': '─',
        '|': '│',
        'F': '┌',
        '7': '┐',
        'L': '└',
        'J': '┘',
        '.': ' ',
    }

    for ii in range(len(inputLines)):
        inputLines[ii] = inputLines[ii].translate(str.maketrans(replacements))

    inputLines = [list(line) for line in inputLines]

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")