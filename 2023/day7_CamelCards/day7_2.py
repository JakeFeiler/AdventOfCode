#!/opt/anaconda3/bin/python
#Jake Feiler

#>250917800

import sys
from collections import defaultdict

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_hand_value(hand):
    '''Encode a value to a hand'''
    #5 of a kind: 90_000_000
    #4 of a kind: 80_000_000
    #Full House: 70_000_000
    #3 of a kind: 60_000_000
    #2 pair: 50_000_000
    #1 pair: 40_000_000
    #High card: 1_000_000 * (value)
    #Tie break: value * 14^x, xth card from back

    hand_value = 0
    card_ranking = "0J23456789TQKA"
    contents = defaultdict(int)

    joker_count = 0
    for card in hand:
        if card == 'J':
            joker_count += 1
        else:
            contents[card] += 1

    if joker_count == 5:
        contents['J'] = 5
    else:
        most_frequent_card = max(contents, key=contents.get)
        contents[most_frequent_card] += joker_count

    card_counts = sorted(contents.values(), reverse=True)

    if card_counts[0] == 5:
        hand_value = 90_000_000
    elif card_counts[0] == 4:
        hand_value = 80_000_000
    elif card_counts[0] == 3:
        if card_counts[1] == 2:
            hand_value = 70_000_000
        else:
            hand_value = 60_000_000
    elif card_counts[0] == 2:
        if card_counts[1] == 2:
            hand_value = 50_000_000
        else:
            hand_value = 40_000_000
    else:
        hand_value = 1_000_000 * (card_ranking.index(hand[0]))

    #Add Tiebreak points
    for pos, card in enumerate(hand):
        hand_value += (13 ** (4 - pos)) * card_ranking.index(card)

    return hand_value

def main():
    s = get_input('input.txt')

    hands_and_bids = []
    for line in s:
        hand, bid = line.split(' ')
        hands_and_bids.append((find_hand_value(hand), int(bid)))

    hands_and_bids.sort(key=lambda x: x[0])

    winnings = 0
    for ranking, bid in enumerate(hands_and_bids):
        #print(ranking,  bid)
        winnings += (ranking + 1)*bid[1]
    print(winnings)


main()
