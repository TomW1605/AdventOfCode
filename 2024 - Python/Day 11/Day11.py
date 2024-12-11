import time
from collections import defaultdict

def blink_pt1(stones):
    new_stones = stones.copy()
    offset = 0
    for ii in range(len(stones)):
        stone_str = str(stones[ii])
        jj = ii + offset
        if stones[ii] == 0:
            new_stones[jj] = 1
        elif len(stone_str) % 2 == 0:
            new_stones[jj] = int(stone_str[0:len(stone_str)//2])
            new_stones.insert(jj+1, int(stone_str[len(stone_str)//2:]))
            offset += 1
        else:
            new_stones[jj] = stones[ii] * 2024
    return new_stones

def part1(input_lines):
    stones = [int(stone) for stone in input_lines[0].split(" ")]
    # print(stones)
    for _ in range(25):
        stones = blink_pt1(stones)
        # print(stones)
    print(len(stones))

def blink_pt2(stones):
    new_stones = defaultdict(int)
    for stone in stones.keys():
        stone_str = str(stone)
        if stone == 0:
            new_stones[1] += stones[0]
        elif len(stone_str) % 2 == 0:
            first_half = int(stone_str[0:len(stone_str)//2])
            new_stones[first_half] += stones[stone]

            second_half = int(stone_str[len(stone_str)//2:])
            new_stones[second_half] += stones[stone]
        else:
            new_val = stone * 2024
            new_stones[new_val] += stones[stone]
    return new_stones

def part2(input_lines):
    stones = {int(stone): 1 for stone in input_lines[0].split(" ")}
    print(stones)
    for _ in range(75):
        stones = blink_pt2(stones)
        # print(stones)
    print(sum(stones.values()))

if __name__ == '__main__':
    test = 0
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
