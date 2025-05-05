#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_next_secret_num(secret_num):
    '''Calculate the next secret number'''
    mix_produce = secret_num * 64
    secret_num = (secret_num ^ mix_produce) % 16777216

    mix_produce = secret_num//32
    secret_num = (secret_num ^ mix_produce) % 16777216

    mix_produce = secret_num * 2048
    secret_num = (secret_num ^ mix_produce) % 16777216

    return secret_num

def main():
    s = get_input('input.txt')

    #Add to the dictionary to track bananas earned by various sequences
    bananas = dd(int)
    for secret_num in s:
        secret_num = int(secret_num)
        #Only track the bananas for the first instance of the sequence found, for this number chain
        found_changes = []
        all_price_changes = []
        for _ in range(2000):
            price = secret_num % 10
            new_secret_num = find_next_secret_num(secret_num)
            new_price = new_secret_num % 10
            price_change = new_price - price

            all_price_changes.append(price_change)
            if len(all_price_changes) >= 4:
                recent_sequence = tuple(all_price_changes[-4:])
                #Encountering the sequence for the first time
                if recent_sequence not in found_changes:
                    found_changes.append(recent_sequence)
                    bananas[recent_sequence] += new_price

            secret_num = new_secret_num

    max_bananas = 0
    for sequence in bananas:
        if bananas[sequence] > max_bananas:
            max_bananas = bananas[sequence]
    print(max_bananas)

main()
