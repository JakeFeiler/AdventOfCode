#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict
import queue

#<6718
def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def map_bag_to_containee(rules):
    '''Create a dictionary mapping each bag to bags that contain it'''
    container = defaultdict(list)
    for rule in rules:
        indiv_bags = rule.replace('.', '').split(' contain')
        container_bag = indiv_bags[0]
        contained_bags = indiv_bags[1].split(',')
        #contained bags have leading space now
        for bag in contained_bags:
            #Keep bag vs bags consistent
            if bag[-1:] == 'g':
                bag = bag + 's'
            container[container_bag].append(bag[1:])
    return container

def count_contained_bags(container, container_bag, bag_count):
    '''Determine how many bags are inside the container_bag'''
    contained_bags = container[container_bag]
    for bag in contained_bags:
        if bag == 'no other bags':
            return 0
        bag_count += int(bag[0]) + int(bag[0]) * count_contained_bags(container, bag[2:], 0)

    return bag_count

def main():
    bag_rules = get_input('input.txt')
    #container maps a bag to bags it contains
    container = map_bag_to_containee(bag_rules)

    print(count_contained_bags(container, 'shiny gold bags', 0))


main()
