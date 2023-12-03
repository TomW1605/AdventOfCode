from readFile import readFile

def part1(input_lines):
    # print(input_lines)

    total = 0
    part_numbers = []
    bad_numbers = []

    for aa in range(0, len(input_lines)):
        line = list(input_lines[aa])
        line.append('.')
        # print(''.join(line))
        for ii in range(0, len(line)):
            if line[ii].isdigit():
                for jj in range(ii, len(line)):
                    if not line[jj].isdigit():
                        # print(line[ii:jj])
                        number = int(''.join(line[ii:jj]))
                        # numbers.append(number)
                        # print(number)
                        line[ii:jj] = '.'*(jj-ii)
                        # print(''.join(line))

                        num_checked = False
                        for bb in range(ii, jj):
                            # if aa != 0 and aa != len(input_lines) and bb != 0 and bb != len(line):
                            for xx in [-1, 0, 1]:
                                for yy in [-1, 0, 1]:
                                    try:
                                        if input_lines[aa+yy][bb+xx] != '.' and not input_lines[aa+yy][bb+xx].isdigit():
                                            # print(input_lines[aa+yy][bb+xx])
                                            # print(number, end='|')
                                            part_numbers.append(number)
                                            num_checked = True
                                            total += number
                                            break
                                    except:
                                        pass

                            if num_checked:
                                # print(number, end='|')
                                # total += number
                                break
                        if not num_checked:
                            # print(number, end='|')
                            bad_numbers.append(number)

                        break

        print(''.join(line))

    print('|'.join(str(v) for v in sorted(part_numbers, reverse=True)))
    print('|'.join(str(v) for v in sorted(bad_numbers, reverse=True)))
    print(total)

def part2(input_lines):
    print('\n'.join(input_lines))
    print()

    total = 0

    for aa in range(0, len(input_lines)):
        line = ['.']
        for place in input_lines[aa]:
            line.append(place)
        line.append('.')
        input_lines[aa] = line

    for aa in range(0, len(input_lines)):
        line = input_lines[aa]
        # print(''.join(line))
        for bb in range(0, len(line)):
            if line[bb] == '*':
                parts = []
                for xx in [-1, 0, 1]:
                    for yy in [-1, 0, 1]:
                        try:
                            if input_lines[aa+yy][bb+xx].isdigit():
                                ii = bb+xx

                                if input_lines[aa+yy][bb+xx+1].isdigit() and input_lines[aa+yy][bb+xx-1].isdigit():
                                    number = int(''.join(input_lines[aa+yy][bb+xx-1:bb+xx+1+1]))
                                    print(number)
                                    parts.append(number)
                                    # print(number)
                                    input_lines[aa+yy][bb+xx-1:bb+xx+1+1] = '.'*3

                                elif input_lines[aa+yy][bb+xx+1].isdigit():
                                    for jj in range(ii, len(input_lines[aa+yy])):
                                        if not input_lines[aa+yy][jj].isdigit():
                                            # print(line[ii:jj])
                                            number = int(''.join(input_lines[aa+yy][ii:jj]))
                                            print(number)
                                            parts.append(number)
                                            # print(number)
                                            input_lines[aa+yy][ii:jj] = '.'*(jj-ii)
                                            break
                                else:
                                    for jj in range(ii, -1, -1):
                                        if not input_lines[aa+yy][jj].isdigit():
                                            # print(line[ii:jj])
                                            number = int(''.join(input_lines[aa+yy][jj+1:ii+1]))
                                            print(number)
                                            parts.append(number)
                                            # print(number)
                                            input_lines[aa+yy][jj+1:ii+1] = '.'*(ii-jj)
                                            break
                        except IndexError:
                            pass

                if len(parts) == 2:
                    total += parts[0]*parts[1]

        # print(''.join(line))

    print(total)


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

