import time

from readFile import readFile

class Hand:
    card_map = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'W': 1
    }

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.card_values = [self.card_map[card] for card in self.cards]
        self.bid = bid
        self.calculate_wildcard()
        self.strength = self.calculate_strength()

    def __str__(self):
        return f"({self.cards}, {self.bid}, {self.strength})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if other.strength != self.strength:
            return other.strength < self.strength

        for ii in range(5):
            if other.card_values[ii] != self.card_values[ii]:
                return other.card_values[ii] < self.card_values[ii]

    def __gt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if other.strength != self.strength:
            return other.strength > self.strength

        for ii in range(5):
            if other.card_values[ii] != self.card_values[ii]:
                return other.card_values[ii] > self.card_values[ii]

    def calculate_wildcard(self):
        if 'W' in self.cards and self.cards != 'WWWWW':
            card_set = set(self.cards)
            card_counts = {card: self.cards.count(card) for card in card_set if card != 'W'}
            best_card = max(card_counts, key=card_counts.get)
            self.cards = self.cards.replace('W', best_card)

    def calculate_strength(self):
        card_set = set(self.cards)
        # print(card_set)

        match len(card_set):
            case 1:
                # print("5 of a kind")
                return 7
            case 2:
                # print("4 of a kind or full house")
                if self.cards.count(card_set.pop()) in [1, 4]:
                    # print("4 of a kind")
                    return 6
                else:
                    # print("full house")
                    return 5
            case 3:
                # print("3 of a kind or 2 pair")
                card_counts = {self.cards.count(card) for card in card_set}
                # print(card_counts)
                if 3 in card_counts:
                    # print("3 of a kind")
                    return 4
                else:
                    # print("2 pair")
                    return 3
            case 4:
                # print("1 pair")
                return 2
            case 5:
                # print("high card")
                return 1

def part1(input_lines):
    print(input_lines)

    hands = [Hand(line.split(' ')[0], int(line.split(' ')[1])) for line in input_lines]
    print(hands)

    # for hand in hands:
    #     hand.calculate_strength()

    hands = sorted(hands, reverse=True)

    total = 0
    for ii in range(len(hands)):
        total += hands[ii].bid * (ii+1)
    print(total)


def part2(input_lines):
    print(input_lines)

    hands = [Hand(line.split(' ')[0].replace('J', 'W'), int(line.split(' ')[1])) for line in input_lines]
    print(hands)

    hands = sorted(hands, reverse=True)

    total = 0
    for ii in range(len(hands)):
        total += hands[ii].bid * (ii+1)
    print(total)


if __name__ == '__main__':
    test = 0
    part = 2

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