#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    machine_count = len(s)//4 + 1
    tokens_needed = 0
    for machine_num in range(machine_count):
        machine_parts = s[machine_num*4: machine_num*4 + 3]
        a = machine_parts[0].split(' ')
        a_x = int(a[2][2:-1])
        a_y = int(a[3][2:])

        b = machine_parts[1].split(' ')
        b_x = int(b[2][2:-1])
        b_y = int(b[3][2:])

        prize = machine_parts[2].split(' ')
        prize_x = int(prize[1][2:-1]) + 10000000000000
        prize_y = int(prize[2][2:]) + 10000000000000



        """
        [a_x b_x] [A B]^T = [prize_x prize_y] T
        [a_y b_y]

        #Invert the first matrix to solve for A,B
        """
        prizes = np.matrix([[prize_x],[prize_y]])
        button_inputs = np.matrix([[a_x, b_x], [a_y, b_y]])
        inverted_inputs = np.linalg.inv(button_inputs)
        button_presses = inverted_inputs*prizes

        #Fortunately, no non-invertable matrices in input (phew)
        #Linalg can cause some rounding issues, make it hard to detect integers
        #Looks like 4 digits is sufficient for accuracy
        a_presses = round(button_presses[0,0], 4)
        b_presses = round(button_presses[1,0], 4)

        if math.floor(a_presses) == a_presses and math.floor(b_presses) == b_presses:
            tokens_needed += 3*int(a_presses) + int(b_presses)
    print(int(tokens_needed))

main()
