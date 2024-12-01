import time

from readFile import readFile

def part1(input_lines):
    list1, list2 = [], []
    for line in input_lines:
        loc_id_1, loc_id_2 = line.split("   ")
        list1.append(int(loc_id_1))
        list2.append(int(loc_id_2))

    list1.sort()
    list2.sort()
    locations = list(zip(list1, list2))
    total = 0
    for location in locations:
        total += abs(location[0] - location[1])

    print(total)

def part2(input_lines):
    list1, list2 = [], []
    for line in input_lines:
        loc_id_1, loc_id_2 = line.split("   ")
        list1.append(int(loc_id_1))
        list2.append(int(loc_id_2))

    similarity = 0
    for loc_id in list1:
        similarity += loc_id * list2.count(loc_id)
    print(similarity)

if __name__ == '__main__':
    test = 0
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
