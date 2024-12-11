import time

import tqdm

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

def blink_pt2(stones, zeros=0, ones=0, twenty_twenty_fours=0):
    new_stones = [20, 24] * twenty_twenty_fours
    twenty_twenty_fours = ones
    ones = zeros
    zeros = 0
    for stone in stones:
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            first_half = int(stone_str[0:len(stone_str)//2])
            second_half = int(stone_str[len(stone_str)//2:])

            if first_half == 0:
                zeros += 1
            elif first_half == 1:
                ones += 1
            elif first_half == 2024:
                twenty_twenty_fours += 1
            else:
                new_stones.append(first_half)

            if second_half == 0:
                zeros += 1
            elif second_half == 1:
                ones += 1
            elif second_half == 2024:
                twenty_twenty_fours += 1
            else:
                new_stones.append(second_half)
        else:
            new_stones.append(stone * 2024)
    return new_stones, zeros, ones, twenty_twenty_fours

def part2(input_lines):
    stones = [int(stone) for stone in input_lines[0].split(" ")]
    zeros = ones = twenty_twenty_fours = 0
    # print(stones)
    # for _ in range(75):
    for _ in (t := tqdm.tqdm(range(75), unit="blinks", postfix={"stones": len(stones),
                                                                "zeros": zeros,
                                                                "ones": ones,
                                                                "2024s": twenty_twenty_fours})):
        stones, zeros, ones, twenty_twenty_fours = blink_pt2(stones, zeros, ones, twenty_twenty_fours)
        t.set_postfix({"stones": len(stones),
                       "zeros": zeros,
                       "ones": ones,
                       "2024s": twenty_twenty_fours})
        # print(stones)
    print(len(stones) + zeros + ones + twenty_twenty_fours)

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
