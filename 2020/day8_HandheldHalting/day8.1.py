#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def run_bootcode(bootcode, acc, line_to_run, visits):
    '''Run line_to_run of bootcode, add the line to visits'''
    if line_to_run in visits:
        return acc
    visits.append(line_to_run)
    line = bootcode[line_to_run]
    operation = line[:3]
    argument = int(line[5:])
    if line[4] == '-':
        argument *= -1
    if operation == 'nop':
        return run_bootcode(bootcode, acc, line_to_run + 1, visits)
    if operation == 'acc':
        return run_bootcode(bootcode, acc + argument, line_to_run + 1, visits)
    #else operation == 'jmp'
    return run_bootcode(bootcode, acc, line_to_run + argument, visits)



def main():
    bootcode = get_input('input.txt')
    repeated_line = run_bootcode(bootcode, 0, 0, [])
    print(repeated_line)

main()
