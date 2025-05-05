#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_value(codes_input, metric):
    '''determine the value of the oxygen or c02'''
    codes = codes_input.copy()
    bit_size = len(codes[0])

    for bit in range(bit_size):
        bit_counter = 0
        if len(codes) == 1:
            return codes[0]
        for code in codes:
            if code[bit] == '1':
                bit_counter += 1
            else:
                bit_counter -= 1
        #filter for 1's if bit_counter >= 0 and oxygen
        #or if bit_counter < 0 and c02
        #otherwise, keep the 0's
        if (bit_counter >= 0 and metric == 'oxygen') or (bit_counter < 0 and metric == 'co2'):
            codes = list(filter(lambda x: x[bit] == '1', codes))
        else:
            codes = list(filter(lambda x: x[bit] == '0', codes))

    if len(codes) == 1:
        return codes[0]
    return 0

def main():
    s = get_input('input.txt')

    oxygen = int(find_value(s, 'oxygen'), 2)
    co2 = int(find_value(s, 'co2'), 2)
    print(oxygen * co2)


main()
