from collections import defaultdict

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
    pairs = defaultdict(lambda: 0)
    template = input_lines[0]
    for ii in range(len(template) - 1):
        pair = template[ii] + template[ii + 1]
        pairs[pair] += 1

    rules = {}
    for line in input_lines[2:]:
        pair, element = line.split(" -> ")
        rules[pair] = element

    print(dict(pairs))
    newPairs = dict(pairs.copy())
    for jj in range(steps):#tqdm(range(steps), unit="steps"):
        #for oldPair in tqdm(range(len(pairs)), leave=False, unit="pairs"):
        #newPairs = {}
        for oldPair in pairs:
            #if pairs[oldPair] <= 0:
            #    continue

            splitPairs = [oldPair[0] + rules[oldPair], rules[oldPair] + oldPair[1]]

            if oldPair in newPairs:
                newPairs[oldPair] -= pairs[oldPair]

            for pair in splitPairs:
                if pair in newPairs:
                    newPairs[pair] += pairs[oldPair]
                else:
                    newPairs[pair] = pairs[oldPair]

        pairs = newPairs.copy()
        print(newPairs)

    letters = defaultdict(lambda: 0)
    letters[template[-1]] = 1
    for letter in pairs:
        number = pairs[letter]
        letters[letter[0]] += number if number > 0 else 0
    print(dict(letters))
    elements = sorted(list(letters.values()))
    print(elements[-1]-elements[0])

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1and2(inputLines, 10)
    elif part == 2:
        part1and2(inputLines, 40)

