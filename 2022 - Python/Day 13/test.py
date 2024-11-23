import ast
import functools
from readFile import readFile

data = inputLines = readFile("test_input_2.txt")

packets = [packet for i in range(1, len(data), 3) for packet in [ast.literal_eval(data[i - 1]), ast.literal_eval(data[i])]]


def Comp(left, right):
    if isinstance(right, list) and not isinstance(left, list):
        left = [left]

    if isinstance(left, list):
        if not isinstance(right, list):
            right = [right]

        for i in range(len(left)):
            if (i >= len(right)):
                return 1

            result = Comp(left[i], right[i])

            if result != 0:
                return result

        if len(left) == len(right):
            return 0

    else:
        return left - right

    return -1


def Part1():
    index = 1
    total = 0

    for i in range(1, len(packets), 2):
        if (Comp(packets[i - 1], packets[i]) < 0):
            print(index)
            total += index

        index += 1

    return total


def Part2():
    div1 = [[2]]
    div2 = [[6]]
    packets.append(div1)
    packets.append(div2)
    sortedPackets = sorted(packets, key=functools.cmp_to_key(Comp))


    for packet in sortedPackets:
        print(packet)

    index1 = sortedPackets.index(div1) + 1
    index2 = sortedPackets.index(div2) + 1

    return index1 * index2


print(Part1())
print(Part2())
