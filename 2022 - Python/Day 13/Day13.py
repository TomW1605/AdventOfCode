import functools

from readFile import readFile


def compare_list(left, right):
    correct = 0
    for ii in range(len(left)):
        if ii in range(len(right)):
            left_item = left[ii]
            right_item = right[ii]

            if type(left_item) == int and type(right_item) == list:
                left_item = [left_item]

            elif type(left_item) == list and type(right_item) == int:
                right_item = [right_item]

            #print(f"{left_item}\t{right_item}")

            if type(left_item) == list and type(right_item) == list:
                correct = compare_list(left_item, right_item)
            elif left_item < right_item:
                correct = 1
                break
            elif left_item > right_item:
                correct = -1
                break
        else:
            correct = -1

        if correct != 0:
            break
    else:
        if len(left) > 0 or len(right) > 0:
            correct = 1
    return correct


def part1(input_lines):
    print(input_lines)
    packets = [[eval(input_lines[ii].strip()), eval(input_lines[ii+1].strip())] for ii in range(0, len(input_lines), 3)]
    print(packets)
    print()

    total_correct = 0
    for ii in range(len(packets)):
        print(f"{packets[ii][0]}\n{packets[ii][1]}")
        if compare_list(packets[ii][0], packets[ii][1]) >= 0:
            print(ii+1)
            total_correct += ii+1
        print()

    print(total_correct)



def part2(input_lines):
    print(input_lines)
    packets = [eval(input_lines[ii].strip()) for ii in range(0, len(input_lines)) if input_lines[ii].strip() != ""]
    divider_start = [[2]]
    divider_end = [[6]]
    packets.append(divider_start)
    packets.append(divider_end)
    print(packets)
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_list))
    print(sorted_packets)

    for packet in sorted_packets:
        print(packet)

    print((sorted_packets.index(divider_start) + 1) * (sorted_packets.index(divider_end) + 1))


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

