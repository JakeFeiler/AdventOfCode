#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    #Create a dictionary to map all machines to their connected parts
    connections = dd(list)
    for machine_pair in s:
        first, second = machine_pair.split('-')
        connections[first].append(second)
        connections[second].append(first)

    #Use this to track t-machines, so as not to double count
    seen_machines = []

    trios = 0
    for machine in connections:
        if machine[0] != 't':
            continue
        seen_machines.append(machine)
        for paired_machine in connections[machine]:
            #Skip any t-machines we've already looked at as basis for trios
            if paired_machine in seen_machines:
                continue
            #Look through THIS machine's connections for a shared connection to starting maachine
            for third_machine in connections[paired_machine]:
                if third_machine in seen_machines:
                    continue
                if machine in connections[third_machine]:
                    trios += 1
        
            
    #We double-counted 1-2-3 and 1-3-2, so divide by 2
    trios /= 2
    print(int(trios))
                  


main()
