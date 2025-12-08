import time

def part1(input_lines):
    print(input_lines)
    input_lines = [list(line) for line in input_lines]

    print("\n".join(["".join(line) for line in input_lines]))
    for ii in range(1, len(input_lines[1:])+1):
        for jj in range(len(input_lines[ii])):
            if input_lines[ii-1][jj] in ["S", "|"]:
                if input_lines[ii][jj] == ".":
                    input_lines[ii][jj] = "|"
                if input_lines[ii][jj] == "^":
                    input_lines[ii][jj-1] = "|"
                    input_lines[ii][jj+1] = "|"
        print("\n".join(["".join(line) for line in input_lines]), end="\n\n")

    splits = 0
    for ii in range(len(input_lines[1:])):
        for jj in range(len(input_lines[ii])):
            if input_lines[ii][jj] == "^":
                if input_lines[ii-1][jj] == "|":
                    splits += 1

    print(splits)
    return splits

def part2(input_lines):
    print(input_lines)

    splits = part1(input_lines) - 1
    timelines = splits * 2
    print(timelines)

if __name__ == '__main__':
    test = 1
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
