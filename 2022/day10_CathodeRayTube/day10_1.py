#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    register = 1
    cycle = 1

    total_signal_strength = 0

    for instruction in s:
        if cycle in (20, 60, 100, 140, 180, 220):
            total_signal_strength += cycle * register

        if instruction == 'noop':
            pass
        else:
            #it's an addx #
            register_change = int(instruction.split(' ')[1])
            register += register_change
            #for addx, add one more cycle and check again
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                total_signal_strength += cycle * register
        cycle += 1




    print(total_signal_strength)





main()
