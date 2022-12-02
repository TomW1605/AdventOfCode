from readFile import readFile


def convert(round_list):
    return [["r" if round.split(" ")[0] == "A" else "p" if round.split(" ")[0] == "B" else "s", "r" if round.split(" ")[1] == "X" else "p" if round.split(" ")[1] == "Y" else "s"] for round in round_list]


def calculate_score(round):
    score = 0

    if round[0] == round[1]:
        score += 3

    if round[1] == "r":
        score += 1
        if round[0] == "s":
            score += 6
    elif round[1] == "p":
        score += 2
        if round[0] == "r":
            score += 6
    elif round[1] == "s":
        score += 3
        if round[0] == "p":
            score += 6

    return score


def part1(input_lines):
    print(input_lines)
    rounds = [["r" if round.split(" ")[0] == "A" else "p" if round.split(" ")[0] == "B" else "s", "r" if round.split(" ")[1] == "X" else "p" if round.split(" ")[1] == "Y" else "s"] for round in input_lines]

    score = 0
    for round in rounds:
        score += calculate_score(round)

    print(score)


def part2(input_lines):
    print(input_lines)
    rounds = [["r" if round.split(" ")[0] == "A" else "p" if round.split(" ")[0] == "B" else "s", "l" if round.split(" ")[1] == "X" else "d" if round.split(" ")[1] == "Y" else "w"] for round in input_lines]

    score = 0
    for round in rounds:
        if round[1] == 'd':
            round[1] = round[0]
        elif round[1] == 'l':
            if round[0] == "r":
                round[1] = "s"
            elif round[0] == "p":
                round[1] = "r"
            elif round[0] == "s":
                round[1] = "p"
        elif round[1] == 'w':
            if round[0] == "r":
                round[1] = "p"
            elif round[0] == "p":
                round[1] = "s"
            elif round[0] == "s":
                round[1] = "r"

        score += calculate_score(round)

    print(score)


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

