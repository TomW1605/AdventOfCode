import math
import re

from readFile import readFile


def part1(cards):
    print(cards)

    total = 0

    for card in cards.values():
        card_points = 0.5
        # print(card['given'])
        for num in card['given']:
            if num in card['winning']:
                card_points *= 2
        # print(math.floor(card_points))
        total += math.floor(card_points)

    print(total)

def part2(cards):
    print(cards)

    total = 0

    for card, card_details in cards.items():
        card_matches = 0
        # print(card['given'])
        for num in card_details['given']:
            if num in card_details['winning']:
                card_matches += 1
        # print(math.floor(card_points))
        if card_matches > 0:
            for ii in range(card+1, card+1+card_matches):
                print(ii)
                cards[ii]['instances'] += card_details['instances']
        total += card_details['instances']

    print(total)


if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    cards = {
        int(re.split(' +', card.split(': ')[0])[1]):
            {
                'winning': [int(x) for x in re.split(' +', card.split(': ')[1].strip().split(' | ')[0].strip())],
                'given': [int(x) for x in re.split(' +', card.split(': ')[1].strip().split(' | ')[1].strip())],
                'instances': 1
            }
        for card in inputLines
    }

    if part == 1:
        part1(cards)
    elif part == 2:
        part2(cards)

