import time

def part1(input_lines):
    print(input_lines)

    line_break_index = input_lines.index("")
    fresh_ranges = [range(int(fresh_range.split('-')[0]), int(fresh_range.split('-')[1])+1) for fresh_range in input_lines[:line_break_index]]
    ingredients = [int(ingredient) for ingredient in input_lines[line_break_index + 1:]]
    print(fresh_ranges)
    print(ingredients)

    count = 0
    for ingredient in ingredients:
        for fresh_range in fresh_ranges:
            if ingredient in fresh_range:
                count += 1
                break

    print(count)



def part2(input_lines):
    print(input_lines)

    line_break_index = input_lines.index("")
    fresh_ranges = [range(int(fresh_range.split('-')[0]), int(fresh_range.split('-')[1])+1) for fresh_range in input_lines[:line_break_index]]

    print(fresh_ranges)
    fresh_ranges = sorted(fresh_ranges, key=lambda x: x.start)
    print(fresh_ranges)

    for ii in range(1, len(fresh_ranges)):
        if fresh_ranges[ii-1].stop > fresh_ranges[ii].start:
            fresh_ranges[ii] = range(fresh_ranges[ii-1].stop, fresh_ranges[ii].stop)
        if fresh_ranges[ii].start > fresh_ranges[ii].stop:
            fresh_ranges[ii] = range(fresh_ranges[ii].start, fresh_ranges[ii].start)

    print(fresh_ranges)
    print(sum([len(fresh_range) for fresh_range in fresh_ranges]))

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
