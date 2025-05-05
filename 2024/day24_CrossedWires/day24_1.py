#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from queue import Queue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    gate_values = {}
    blank_line = s.index('')

    for initial_wire in s[:blank_line]:
        name, value = initial_wire.split(': ')
        gate_values[name] = bool(int(value))

    #Run a queue of all pairs, until they've been satisfied
    gates = Queue()
    for gate in s[blank_line + 1:]:
        gates.put(gate)

    while not gates.empty():
        next_gate_unsplit = gates.get()
        next_gate = next_gate_unsplit.split(' ')
        input_one, input_two = next_gate[0], next_gate[2]
        command = next_gate[1]
        destination = next_gate[4]
        #Set the next value accordingly if possible
        try:
            value_one, value_two = gate_values[input_one], gate_values[input_two]
            if command == 'AND':
                gate_values[destination] = value_one and value_two
            elif command == 'OR':
                gate_values[destination] = value_one or value_two
            else:
                #XOR
                gate_values[destination] = (value_one != value_two)
        #If a value is missing, append the instruction, try again later
        except:
            gates.put(next_gate_unsplit)

    output = 0
    for gate in gate_values:
        if gate[0] == 'z':
            output += gate_values[gate] * (2**int(gate[1:]))
    print(output)
main()

