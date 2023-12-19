import time

from readFile import readFile

def part1(input_lines):
    # print(input_lines)

    workflows = []
    temp = []
    for line in input_lines:
        if line == '':
            workflows = temp[:]
            temp = []
        else:
            temp.append(line)
    parts = temp[:]

    parts = [(f"{{'x': {part.split(',')[0].split('=')[1]}, "
              f"'m': {part.split(',')[1].split('=')[1]}, "
              f"'a': {part.split(',')[2].split('=')[1]}, "
              f"'s': {part.split(',')[3].split('=')[1].replace('}', '')}}}") for part in parts]
    parts = f"[{', '.join(parts)}]"
    # print(parts)

    # print(workflows)
    functions = ("accepted = []\n"
                 "rejected = []\n"
                 "def A(part):\n"
                 "    accepted.append(part)\n\n"
                 "def R(part):\n"
                 "    rejected.append(part)\n\n")
    for ii in range(len(workflows)):
        workflow = workflows[ii]

        name = workflow.split('{')[0]
        name = name if name != 'in' else 'in_'
        steps = workflow.split('{')[1].split(',')[:-1]
        # print(steps)

        elif_section = '\n'.join([f"    elif part['{step[0]}']{step.split(':')[0][1:]}:\n"
                                  f"        {step.split(':')[1]}(part)\n" for step in steps[1:]])

        workflow_function = (f"def {name}(part):\n"
                             f"    if part['{steps[0][0]}']{steps[0].split(':')[0][1:]}:\n"
                             f"        {steps[0].split(':')[1]}(part)\n"
                             f"{elif_section}"
                             f"    else:\n"
                             f"        {workflow.split(',')[-1].replace('}', '')}(part)\n\n")
        # print(workflow_function)
        functions += workflow_function

    # print(functions)

    full_code = functions + (f"for part in {parts}:\n"
                             f"    in_(part)\n\n"
                             f"print(accepted)\n"
                             f"print(rejected)\n"
                             f"print(sum([sum(part.values()) for part in accepted]))\n")

    print(full_code)
    # exec(full_code)
    f = open("output.py", "w")
    f.write(full_code)
    f.close()

    import output


def part2(input_lines):
    print(input_lines)


if __name__ == '__main__':
    test = 0
    part = 1

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