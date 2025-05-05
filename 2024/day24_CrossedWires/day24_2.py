#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from queue import Queue
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def make_a_bit(z_gate_value, carry_gate, switches, gate_patterns):
    '''Run the calculations to make middle bits'''
    #See notes.txt for details
    #Assumption/Hope, no equation is using 2 or 3 incorrect gates
    x_gate = 'x' + z_gate_value[1:]
    y_gate = 'y' + z_gate_value[1:]
    xy_and_gate = ''
    xy_xor_gate = ''
    for pattern in gate_patterns:
        if (x_gate + ' AND ' + y_gate) in pattern or (y_gate + ' AND ' + x_gate) in pattern:
            xy_and_gate = pattern[-3:]
        if (x_gate + ' XOR ' + y_gate) in pattern or (y_gate + ' XOR ' + x_gate) in pattern:
            xy_xor_gate = pattern[-3:]
            


    #Look for the xor of carry_gate and xy_xor gate
    gate_found = False
    xor_string_1 = switches[carry_gate] + ' XOR ' + switches[xy_xor_gate]
    xor_string_2 = switches[xy_xor_gate] + ' XOR ' + switches[carry_gate]
    for pattern in gate_patterns:
        if xor_string_1 in pattern or xor_string_2 in pattern:
            gate_found = True
            z_dest_gate = pattern[-3:]
            #The z gate is wrong
            if z_dest_gate != z_gate_value:
                switches[z_dest_gate] = z_gate_value
                switches[z_gate_value] = z_dest_gate
            break

    #Couldn't find it, an input's wrong
    if not gate_found:
        for pattern in gate_patterns:
            if 'XOR' in pattern and pattern[-3:] == z_gate_value:
                pattern = pattern[:-7]
                if pattern[:3] == carry_gate or pattern[-3:] == carry_gate:
                    wrong_gate = xy_xor_gate
                else:
                    wrong_gate = carry_gate
                if pattern[:3] == carry_gate or pattern[:3] == xy_xor_gate:
                    new_gate = pattern[-3:]
                else:
                    new_gate = pattern[3:]
                switches[new_gate] = wrong_gate
                switches[wrong_gate] = new_gate

    #Look for the & of carry and xy_xor
    gate_found = False
    and_string_1 = switches[carry_gate] + ' AND ' + switches[xy_xor_gate]
    and_string_2 = switches[xy_xor_gate] + ' AND ' + switches[carry_gate]
    for pattern in gate_patterns:
        if and_string_1 in pattern or and_string_2 in pattern:
            next_carry_checker = pattern[-3:]
            gate_found = True
            break

    #Couldn't find it, an input's wrong
    if not gate_found:
        for pattern in gate_patterns:
            if pattern [:8] == (xy_xor_gate + ' AND'):
                wrong_gate = carry_gate
                new_gate = pattern[8:12]
                next_carry_checker = pattern[-3:]
            elif pattern[4:12] == ('AND ' + xy_xor_gate):
                wrong_gate = carry_gate
                new_gate = pattern[:4]
                next_carry_checker = pattern[-3:]
            elif pattern [:8] == (carry_gate + ' AND'):
                wrong_gate = xy_xor_gate
                new_gate = pattern[8:12]
                next_carry_checker = pattern[-3:]
            elif pattern[4:12] == ('AND ' + carry_gate):
                wrong_gate = xy_xor_gate
                new_gate = pattern[:4]
                next_carry_checker = pattern[-3:]

        #Switch the wrong input
        switches[new_gate] = wrong_gate
        switches[wrong_gate] = new_gate


    #One final time, with the new carry gate
    #Look for the OR of next_carry_checker and xy_and_gate
    gate_found = False
    or_string_1 = switches[next_carry_checker] + ' OR ' + switches[xy_and_gate]
    or_string_2 = switches[xy_and_gate] + ' OR ' + switches[next_carry_checker]
    for pattern in gate_patterns:
        if or_string_1 in pattern or or_string_2 in pattern:
            new_carry= pattern[-3:]
            gate_found = True
            break

    #Couldn't find it, an input's wrong
    if not gate_found:
        for pattern in gate_patterns:
            if pattern [:7] == (xy_and_gate + ' OR'):
                wrong_gate = next_carry_checker
                new_gate = pattern[7:11]
                new_carry = pattern[-3:]
            elif pattern[4:11] == ('OR ' + xy_and_gate):
                wrong_gate = next_carry_checker
                new_gate = pattern[:4]
                new_carry = pattern[-3:]
            elif pattern [:7] == (next_carry_checker + ' OR'):
                wrong_gate = xy_and_gate
                new_gate = pattern[7:11]
                new_carry = pattern[-3:]
            elif pattern[4:11] == ('OR ' + next_carry_checker):
                wrong_gate = xy_and_gate
                new_gate = pattern[:4]
                new_carry = pattern[-3:]

        #Switch the wrong input
        switches[new_gate] = wrong_gate
        switches[wrong_gate] = new_gate

    return new_carry, switches


def main():
    s = get_input('input.txt')
    gate_values = {}
    blank_line = s.index('')
    gate_patterns = s[blank_line + 1:]

    #Use this to track wrong switches, most will point to itself
    max_z = 0
    switches = dd(str)
    for pattern in gate_patterns:
        gates = pattern.split(' ')
        input_one, input_two, output = gates[0], gates[2], gates[4]
        switches[input_one] = input_one
        switches[input_two] = input_two
        switches[output] = output
        if output[0] == 'z':
            max_z = max(max_z, int(output[1:]))


    #Analysis -> y00 XOR x00 -> z00 in input
    #Take the carry gate with AND, start feeding that into recursion
    for pattern in gate_patterns:
        if 'x00 AND y00' in pattern or 'y00 and x00' in pattern:
            carry_gate = pattern[-3:]

    for z_gate in range(1, max_z):
    #for z_gate in range(1, 3):
        if z_gate < 10:
            z_gate_string = '0' + str(z_gate)
        else:
            z_gate_string = str(z_gate)
        carry_gate, switches = make_a_bit('z' + z_gate_string, carry_gate, switches, gate_patterns)

    wrong_switches = []
    for switch in switches:
        if switches[switch] != switch:
            wrong_switches.append(switch)
    wrong_switches.sort()
    print(','.join(wrong_switches))
main()
