from readFile import readFile


def part1(input_lines):
    print(input_lines)

    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    total = 0

    for game, rounds in input_lines.items():
        impossible = False
        for game_round in rounds:
            if 'red' in game_round.keys():
                if game_round['red'] > max_cubes['red']:
                    impossible = True
                    break

            if 'green' in game_round.keys():
                if game_round['green'] > max_cubes['green']:
                    impossible = True
                    break

            if 'blue' in game_round.keys():
                if game_round['blue'] > max_cubes['blue']:
                    impossible = True
                    break

        if impossible:
            continue

        total += game

    print(total)


def part2(input_lines):
    print(input_lines)

    total_power = 0

    for game, rounds in input_lines.items():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for game_round in rounds:
            if 'red' in game_round.keys():
                if game_round['red'] > min_cubes['red']:
                    min_cubes['red'] = game_round['red']

            if 'green' in game_round.keys():
                if game_round['green'] > min_cubes['green']:
                    min_cubes['green'] = game_round['green']

            if 'blue' in game_round.keys():
                if game_round['blue'] > min_cubes['blue']:
                    min_cubes['blue'] = game_round['blue']

        total_power += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    print(total_power)

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    games = {int(line.split(": ")[0].split()[1]): [{cube.split()[1]: int(cube.split()[0]) for cube in game_round.split(", ")} for game_round in line.split(": ")[1].split("; ")] for line in inputLines}

    # print(games)

    if part == 1:
        part1(games)
    elif part == 2:
        part2(games)

