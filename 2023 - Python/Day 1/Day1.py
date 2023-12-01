from readFile import readFile


def part1(input_lines):
    print(input_lines)
    total = 0
    for line in input_lines:
        # print(line)
        number = ""
        for ii in range(0, line.__len__()):
            if line[ii].isdigit():
                number += line[ii]
                break
        for ii in range(line.__len__()-1, -1, -1):
            if line[ii].isdigit():
                number += line[ii]
                break
        print(number)
        total += int(number)
    print(total)


def part2(input_lines):
    print(input_lines)
    spelled_nums = {
        "one": "1__",
        "two": "2__",
        "three": "3____",
        "four": "4___",
        "five": "5___",
        "six": "6__",
        "seven": "7____",
        "eight": "8____",
        "nine": "9___"}
    total = 0
    for xx in range(0, input_lines.__len__()):
        line = input_lines[xx]
        print(line)

        # for num in spelled_nums.keys():
        #     line = line.replace(spelled_nums[num], num)

        done = False
        for ii in range(0, line.__len__()):
            for jj in range(ii, line.__len__()):
                if line[ii].isdigit():
                    done = True
                    break
                # print(line[ii:jj+1])
                if line[ii:jj+1] in spelled_nums.keys():
                    line = line.replace(line[ii:jj+1], spelled_nums[line[ii:jj+1]], 1)
                    done = True
                    break
            if done:
                break

        done = False
        for ii in range(line.__len__()-1, -1, -1):
            if line[ii].isdigit() or line[ii] == "_":
                break
            for jj in range(ii, -1, -1):
                # print(f"{ii}:{jj-1}")
                # print(line[jj:ii+1])
                if line[jj:ii+1] in spelled_nums.keys():
                    line = line.replace(line[jj:ii+1], spelled_nums[line[jj:ii+1]])
                    done = True
                    break
            if done:
                break

        print(line)
        number = ""
        for ii in range(0, line.__len__()):
            if line[ii].isdigit():
                number += line[ii]
                break
        for ii in range(line.__len__()-1, -1, -1):
            if line[ii].isdigit():
                number += line[ii]
                break
        print(number)
        total += int(number)

    print(total)
    # part1(input_lines)


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

