#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def run_bootcode(bootcode, acc, line_to_run, visits, has_flipped):
    '''Run line_to_run of bootcode, add the line to visits'''
    #Everytime nop or jmp is found, try a run with the operation flipped
    if line_to_run in visits:
        return -1
    visits.append(line_to_run)
    try:
        line = bootcode[line_to_run]
    except:
        #success, program has reached end
        return acc
    operation = line[:3]
    argument = int(line[5:])
    if line[4] == '-':
        argument *= -1
    if operation == 'nop':
        if not has_flipped:
            return max(run_bootcode(bootcode, acc, line_to_run + 1, visits, False), run_bootcode(bootcode, acc, line_to_run + argument, visits, True))
        #else, already did a flip, so run normally
        return run_bootcode(bootcode, acc, line_to_run + 1, visits, True)
    if operation == 'acc':
        return run_bootcode(bootcode, acc + argument, line_to_run + 1, visits, has_flipped)
    
    #else operation == 'jmp'
    if not has_flipped:
        return max(run_bootcode(bootcode, acc, line_to_run + argument, visits, False), run_bootcode(bootcode, acc, line_to_run + 1, visits, True))
    else:
        return run_bootcode(bootcode, acc, line_to_run + argument, visits, True)



def main():
    bootcode = get_input('input.txt')
    repeated_line = run_bootcode(bootcode, 0, 0, [], False)
    print(repeated_line)

main()
