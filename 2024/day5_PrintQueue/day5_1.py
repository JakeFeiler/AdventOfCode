#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def is_valid(update, rule_orders):
    '''Return if the update fits the rules'''
    #False if the second page has the first in it's dictionary
    for former_pos, former in enumerate(update):
        for latter in update[former_pos+1:]:
            if former in rule_orders[latter]:
                return False
    return True

def main():
    s = get_input('input.txt')
    empty_line = s.index('')
    rules, updates = s[:empty_line], s[empty_line + 1:]
        

    rule_orders = dd(list)
    for rule in rules:
        #All rules are 2-digit numbers
        #Set up the dictionary
        rule_orders[''.join(rule[:2])].append(''.join(rule[-2:]))

    good_update_values = 0
    for update in updates:
        update = update.split(',')
        if is_valid(update, rule_orders):
            good_update_values += int(update[len(update)//2])

    print(good_update_values)



main()
