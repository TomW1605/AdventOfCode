from dataclasses import dataclass, field
from typing import List

from readFile import readFile

hexMap = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

class Packet:
    pass

@dataclass
class Packet:
    version: int = -1
    typeID: int = -1
    lenTypeID: int = -1
    content: List = field(default_factory=lambda: [])
    value: int = -1

def parseBITS(inputBITS):
    binary = ""
    for letter in list(inputBITS):
        binary += hexMap[letter]
    return binary

def splitAtIndex(text: str, index: int):
    return text[:index], text[index:]

def parsePackets(binary: str):
    #print(binary)
    if '1' not in binary:
        return None, None
    packet = Packet()
    version, binary = splitAtIndex(binary, 3)
    packet.version = int(version, 2)
    typeID, binary = splitAtIndex(binary, 3)
    packet.typeID = int(typeID, 2)
    #print(packet.version, packet.typeID)

    if packet.typeID == 4:
        #print("value")
        valueStr = ""
        valueSubStr, binary = splitAtIndex(binary, 5)
        valueStr += valueSubStr[1:]
        while valueSubStr[0] == '1':
            valueSubStr, binary = splitAtIndex(binary, 5)
            valueStr += valueSubStr[1:]
        packet.value = int(valueStr, 2)
    else:
        lenTypeID, binary = splitAtIndex(binary, 1)
        packet.lenTypeID = int(lenTypeID, 2)
        if packet.lenTypeID:
            num, binary = splitAtIndex(binary, 11)
            while len(packet.content) < int(num, 2):
                newPacket, binary = parsePackets(binary)
                packet.content.append(newPacket)
        else:
            length, binary = splitAtIndex(binary, 15)
            contentBinary, binary = splitAtIndex(binary, int(length, 2))
            while len(contentBinary) > 0:
                newPacket, contentBinary = parsePackets(contentBinary)
                packet.content.append(newPacket)

    return packet, binary

def processPackets(packet: Packet, depth: int = 0):

    match packet.typeID:
        case 0:
            print("\t"*depth + "sum {")
            subTotal = 0
            for subPacket in packet.content:
                subTotal += processPackets(subPacket, depth+1)
            print("\t"*depth + "} =", subTotal)
        case 1:
            print("\t"*depth + "product {")
            subTotal = 1
            for subPacket in packet.content:
                subTotal *= processPackets(subPacket, depth+1)
            print("\t"*depth + "} =", subTotal)
        case 2:
            print("\t"*depth + "minimum {")
            subTotal = min([processPackets(subPacket, depth+1) for subPacket in packet.content])
            print("\t"*depth + "} =", subTotal)
        case 3:
            print("\t"*depth + "maximum {")
            subTotal = max([processPackets(subPacket, depth+1) for subPacket in packet.content])
            print("\t"*depth + "} =", subTotal)
        case 4:
            subTotal = packet.value
            print("\t"*depth + "value:", subTotal)
        case 5:
            print("\t"*depth + "greater than {")
            for subPacket in packet.content:
                processPackets(subPacket, depth+1)
            subTotal = int(packet.content[0].value > packet.content[1].value)
            print("\t"*depth + "} =", subTotal)
        case 6:
            print("\t"*depth + "less than {")
            for subPacket in packet.content:
                processPackets(subPacket, depth+1)
            subTotal = int(packet.content[0].value < packet.content[1].value)
            print("\t"*depth + "} =", subTotal)
        case 7:
            print("\t"*depth + "equal to {")
            for subPacket in packet.content:
                processPackets(subPacket, depth+1)
            subTotal = int(packet.content[0].value == packet.content[1].value)
            print("\t"*depth + "} =", subTotal)

    packet.value = subTotal
    return subTotal

def sumVersions(packet: Packet):
    subTotal = 0
    for subPacket in packet.content:
        subTotal += sumVersions(subPacket)
    subTotal += packet.version
    return subTotal

def part1(input_lines):
    binary = parseBITS(input_lines[0])
    packet = parsePackets(binary)[0]
    output = sumVersions(packet)
    print(output)

def part2(input_lines):
    binary = parseBITS(input_lines[0])
    packet = parsePackets(binary)[0]
    output = processPackets(packet)
    print(output)

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

