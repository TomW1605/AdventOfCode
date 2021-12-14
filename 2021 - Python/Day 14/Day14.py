from tqdm import tqdm

#from readFile import readFile
def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

def part1and2(input_lines, steps):
    print(input_lines)
    pairs = {}
    template = input_lines[0]
    for ii in range(len(template) - 1):
        pair = template[ii] + template[ii + 1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    rules = {}
    for line in input_lines[2:]:
        pair, element = line.split(" -> ")
        rules[pair] = element

    print(pairs)
    newPairs = {}
    for jj in tqdm(range(steps), unit="steps"):
        #for oldPair in tqdm(range(len(pairs)), leave=False, unit="pairs"):
        newPairs = {}
        for oldPair in pairs:
            if pairs[oldPair] <= 0:
                continue

            splitPairs = [oldPair[0] + rules[oldPair], rules[oldPair] + oldPair[1]]

            if oldPair in newPairs:
                newPairs[oldPair] -= pairs[oldPair]
            else:
                newPairs[oldPair] = 0

            for pair in splitPairs:
                if pair in newPairs:
                    newPairs[pair] += 1
                elif pair in pairs:
                    newPairs[pair] = pairs[pair] * 2
                else:
                    newPairs[pair] = 1
        pairs = newPairs.copy()
        print(pairs)

    letters = {}
    #{letter[0]: number if letter[0] in self.keys() else  for letter, number in pairs}
    for letter in pairs:
        number = pairs[letter]
        if letter[0] in letters.keys():
            letters[letter[0]] += number if number > 0 else 0
        else:
            letters[letter[0]] = number if number > 0 else 0
    print(letters)
    elements = sorted(list(letters.values()))
    print(elements[-1]-elements[0])

if __name__ == '__main__':
    test = 1
    part = 1

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1and2(inputLines, 4)
    elif part == 2:
        part1and2(inputLines, 40)

