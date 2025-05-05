#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict
import queue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def map_bag_to_container(rules):
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
            container[bag[3:]].append(container_bag)
    return container

def count_shiny_gold_bag_containers(container):
    '''Determine how many bags directly or indirectly have shiny gold bags'''
    bag_list = set()
    recursive_bags = queue.Queue()
    recursive_bags.put('shiny gold bags')
    #Put shiny gold bags in the queue
    #Keep on putting the bags that contain bags in the queue into the queue
    while not recursive_bags.empty():
        bag = recursive_bags.get()
        for container_bag in container[bag]:
            bag_list.add(container_bag)
            recursive_bags.put(container_bag)


    return len(bag_list)

def main():
    bag_rules = get_input('input.txt')
    #container maps a bag to all bags that directly contain it
    container = map_bag_to_container(bag_rules)

    print(count_shiny_gold_bag_containers(container))


main()
