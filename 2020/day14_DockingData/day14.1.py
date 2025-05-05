#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    instructions = get_input('input.txt')
    memory = {}
    mask = 0
    for instruction in instructions:
        if instruction[:3] == 'mem':
            #mask apply to mem
            instruction_parts = instruction.split(' ')
            unmasked_value = str(bin(int(instruction_parts[2])))[2:]
            unmasked_value = '0'*(36 - len(unmasked_value)) + unmasked_value
            masked_value = 0
            for inverse_power, digit in enumerate(mask):
                if digit == '1':
                    masked_value += (1 << (35 - inverse_power))
                elif digit == 'X':
                    masked_value += (int(unmasked_value[inverse_power]) << (35 - inverse_power))
                else:
                    #digit == '0'
                    continue

            position = int(instruction_parts[0][4:-1])
            memory[position] = masked_value
        else:
            mask = instruction[7:]

    total = sum(memory.values())
    print(total)

main()
