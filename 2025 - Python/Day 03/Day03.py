import itertools
import math
import time

from tqdm import tqdm

def part1(input_lines):
    print(input_lines)

    total = 0
    for bank in input_lines:
        total += max([int(''.join(pair)) for pair in itertools.combinations(bank, 2)])

    print(total)

def part2(input_lines):
    print(input_lines)

    total_len = 12
    total = 0
    # for bank in input_lines:
    for bank in tqdm(input_lines, unit="bank"):
        bank = [int(battery) for battery in bank]
        value = ""
        search_index = 0
        while search_index < len(bank) and len(value) < total_len:
            search_index = bank.index(max(bank[search_index:len(bank) + len(value) - total_len + 1]), search_index)
            value += str(bank[search_index])
            search_index += 1
        total += int(value)

    print(total)

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
