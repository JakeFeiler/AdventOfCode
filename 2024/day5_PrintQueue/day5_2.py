#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd
from functools import cmp_to_key

RULE_ORDERS = dd(list)

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def is_valid(update):
    '''Return if the update fits the rules'''
    global RULE_ORDERS
    #False if the second page has the first in it's dictionary
    for former_pos, former in enumerate(update):
        for latter in update[former_pos+1:]:
            if former in RULE_ORDERS[latter]:
                return False
    return True

def following(entry_one, entry_two):
    global RULE_ORDERS
    if entry_two in RULE_ORDERS[entry_one]:
        return 1
    elif entry_one in RULE_ORDERS[entry_two]:
        return -1
    else:
        return 0

def sort_update(update):
    '''Return if the update fits the rules'''
    fixed_update = sorted(update, key=cmp_to_key(following))
    return fixed_update
           
def main():
    s = get_input('input.txt')
    empty_line = s.index('')
    rules, updates = s[:empty_line], s[empty_line + 1:]
        

    global RULE_ORDERS
    for rule in rules:
        #All rules are 2-digit numbers
        #Set up the dictionary
        RULE_ORDERS[''.join(rule[:2])].append(''.join(rule[-2:]))

    good_update_values = 0
    for update in updates:
        update = update.split(',')
        if not is_valid(update):
            fixed_update = sort_update(update)
            good_update_values += int(fixed_update[len(fixed_update)//2])

    print(good_update_values)



main()
