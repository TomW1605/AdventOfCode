import time

def move_bot(grid, bot, move):
    y, x = bot
    dy, dx = move
    ii = 0
    while grid[y + dy * ii][x + dx * ii] not in ["#", "."]:
        ii += 1
        # if grid[y + dy * (ii-1)][x + dx * (ii-1)] == ".":
        #     break
    if grid[y + dy * ii][x + dx * ii] == "#":
        return grid, bot
    elif grid[y + dy * ii][x + dx * ii] == ".":
        for jj in range(ii, 0, -1):
            grid[y + dy * jj][x + dx * jj] = grid[y + dy * (jj-1)][x + dx * (jj-1)]
        grid[y][x] = "."
        return grid, (y + dy, x + dx)
    return grid, bot

def part1(input_lines):
    input_text = "\n".join(input_lines)
    grid_text, moves = input_text.split("\n\n")
    moves = moves.replace("\n", "")
    grid = [list(line) for line in grid_text.split("\n")]
    bot = (0, 0)
    for row in grid:
        if "@" in row:
            bot = (grid.index(row), row.index("@"))
            break
    print(bot)

    # print("Initial state:")
    print("".join(["".join(row) + "\n" for row in grid]), end="\n")
    for move in moves:
        # print(f"Move {move}:")
        match move:
            case "^":
                grid, bot = move_bot(grid, bot, (-1, 0))
            case "v":
                grid, bot = move_bot(grid, bot, (1, 0))
            case "<":
                grid, bot = move_bot(grid, bot, (0, -1))
            case ">":
                grid, bot = move_bot(grid, bot, (0, 1))

    print("".join(["".join(row) + "\n" for row in grid]), end="\n")

    total = 0
    for ii in range(len(grid)):
        for jj in range(len(grid[0])):
            if grid[ii][jj] == "O":
                total += ii * 100 + jj
    print(total)

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 0
    part = 1

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
