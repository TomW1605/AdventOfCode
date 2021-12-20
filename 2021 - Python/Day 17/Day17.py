from dataclasses import dataclass

from readFile import readFile

@dataclass
class point:
    x: int = 0
    y: int = 0
    xVelocity: int = 0
    yVelocity: int = 0

def part1(input_lines):
    print(input_lines)
    input_line = input_lines[0].split()
    xRange = [int(xBorder) for xBorder in input_line[2].lstrip("x=").rstrip(",").split("..")]
    yRange = [int(yBorder) for yBorder in input_line[3].lstrip("y=").split("..")]

    yVel = abs(yRange[0])-1

    print(yVel*(yVel+1)//2)

def moveProbe(xPos, yPos, xVelocity, yVelocity):
    xPos += xVelocity
    yPos += yVelocity

    if xVelocity > 0:
        xVelocity -= 1
    elif xVelocity < 0:
        xVelocity += 1
    else:
        xVelocity = 0

    yVelocity -= 1

    return xPos, yPos, xVelocity, yVelocity

def part2(input_lines):
    print(input_lines)
    input_line = input_lines[0].split()
    xRange = [int(xBorder) for xBorder in input_line[2].lstrip("x=").rstrip(",").split("..")]
    yRange = [int(yBorder) for yBorder in input_line[3].lstrip("y=").split("..")]

    hits = set()
    for xTest in range(0, 300):
        for yTest in range(-300, 300):
            xPos = 0
            yPos = 0
            xVelocity = xTest
            yVelocity = yTest
            while xPos < xRange[1] and yPos > yRange[0]:
                xPos, yPos, xVelocity, yVelocity = moveProbe(xPos, yPos, xVelocity, yVelocity)
                if xRange[0] <= xPos <= xRange[1] and yRange[0] <= yPos <= yRange[1]:
                    hits.add((xTest, yTest))
                    print((xTest, yTest))

    print(len(hits))

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

