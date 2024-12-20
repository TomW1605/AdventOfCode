import re
import time

import tqdm

def part1(input_lines):
    towels = input_lines[0].split(", ")
    towels.sort(key=lambda s: len(s), reverse=True)
    print(len(towels), towels)
    useful_towels = towels.copy()
    for towel in towels:
        temp_towels = towels.copy()
        temp_towels.remove(towel)
        if re.search(f"^(?:{'|'.join(temp_towels)})*$", towel):
            useful_towels.remove(towel)
    print(len(useful_towels), useful_towels)
    designs = input_lines[2:]
    regex = re.compile(f"^(?:{'|'.join(useful_towels)})*$")
    print(regex.pattern)
    possible_designs = []
    for design in designs:
    # for ii in tqdm.tqdm(range(len(designs))):
        # print(ii)
        # design = designs[ii]
        # print(design)
        if regex.search(design):
            possible_designs.append(design)
    # matches = re.findall(f"^(?:{'|'.join(towels)})*$", designs, re.MULTILINE)
    # print(matches)
    print(len(possible_designs))

def part2(input_lines):
    towels = input_lines[0].split(", ")
    towels.sort(key=lambda s: len(s), reverse=True)

    print(len(towels), towels)
    useful_towels = towels.copy()
    for towel in towels:
        temp_towels = towels.copy()
        temp_towels.remove(towel)
        if re.search(f"^(?:{'|'.join(temp_towels)})*$", towel):
            useful_towels.remove(towel)
    print(len(useful_towels), useful_towels)

    designs = input_lines[2:]
    regex = re.compile(f"^(?:{'|'.join(useful_towels)})*$")
    print(regex.pattern)
    possible_designs = []
    # for design in designs:
    for ii in tqdm.tqdm(range(len(designs))):
        design = designs[ii]
        if regex.search(design):
            possible_designs.append(design)

    total_options = 0
    regex = re.compile(f"(?=^(?:{'|'.join(towels)})*$)")
    # for design in possible_designs:
    for ii in (t := tqdm.tqdm(range(len(possible_designs)), postfix={"total_options": total_options})):
        design = possible_designs[ii]
        options = regex.findall(design)
        total_options += len(options)
        t.set_postfix(total_options=total_options)
    print(total_options)

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
