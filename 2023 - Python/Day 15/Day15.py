import re
import time

from readFile import readFile

def calculate_hash(current_value, string):
    current_value += ord(string[0])
    current_value *= 17
    current_value %= 256
    if len(string) > 1:
        return calculate_hash(current_value, string[1:])
    return current_value

class Lens:
    def __init__(self, label, focal_len):
        self.label = label
        if focal_len == '':
            self.focal_len = 0
        else:
            self.focal_len = int(focal_len)

    def __str__(self):
        return f"[{self.label} {str(self.focal_len)}]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Lens):
            return self.label == other.label
        return NotImplemented

def part1(input_lines):
    print(input_lines)

    sequence = input_lines[0].split(',')

    print(sum(calculate_hash(0, step) for step in sequence))

def part2(input_lines):
    print(input_lines)

    sequence = [Lens(*re.split('[=\-]', step)) for step in input_lines[0].split(',')]

    print(sequence)

    boxes = [[] for _ in range(256)]
    # print([box for box in boxes if box != []])

    for lens in sequence:
        box_id = calculate_hash(0, lens.label)

        if lens.focal_len:
            # print('insert')
            if lens in boxes[box_id]:
                boxes[box_id][boxes[box_id].index(lens)] = lens
            else:
                boxes[box_id].append(lens)
        elif lens in boxes[box_id]:
            boxes[box_id].remove(lens)

    print(sum([sum([(box_id+1)*(lens_id+1)*boxes[box_id][lens_id].focal_len for lens_id in range(len(boxes[box_id]))]) for box_id in range(len(boxes)) if boxes[box_id] != []]))

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