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
            unmasked_position = str(bin(int(instruction_parts[0][4:-1])))[2:]
            value = int(instruction_parts[2])
            unmasked_position = '0'*(36 - len(unmasked_position)) + unmasked_position
            positions = [0]
            for inverse_power, digit in enumerate(mask):
                if digit == '1':
                    for position in range(len(positions)):
                        positions[position] += (1 << (35 - inverse_power))
                elif digit == '0':
                    for position in range(len(positions)):
                        positions[position] += (int(unmasked_position[inverse_power]) << (35 - inverse_power))
                else: #digit = 'x'
                    new_spots = positions.copy()
                    #new_spots has 0 shifted on
                    for position in range(len(positions)):
                        positions[position] += (1 << (35 - inverse_power))
                    positions = positions + new_spots
            for position in positions:
                memory[position] = value
        else:
            mask = instruction[7:]

    total = sum(memory.values())
    print(total)

main()
