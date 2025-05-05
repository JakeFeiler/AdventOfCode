#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    overlappings = 0
    for pairing in s:
        elf_1, elf_2 = pairing.split(',')
        elf_1_start, elf_1_stop = map(int, elf_1.split('-'))
        elf_2_start, elf_2_stop = map(int, elf_2.split('-'))
        if (elf_1_start >= elf_2_start and elf_1_stop <= elf_2_stop) \
        or (elf_1_start <= elf_2_start and elf_1_stop >= elf_2_stop):
            overlappings += 1

    print(overlappings)

main()
