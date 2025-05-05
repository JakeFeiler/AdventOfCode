#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from itertools import permutations, chain

#Bad brute force method, try all and look for shortes

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_keypad_sequence(code):
    '''Determine the sequence the first robot must enter'''
    keypad = {}
    for value in range(9,0,-1):
        row = (value + 2)//3
        col = (value - 1)%3
        keypad[str(value)] = col + row*1j
    keypad['0'] = 1
    keypad['A'] = 2

    final_sequences = ['']
    #Begin at A, move from last pressed key
    prev_button = 'A'
    for button in code:
        #Always moving from the A
        distance = keypad[button] - keypad[prev_button]
        x, y = int(distance.real), int(distance.imag)
        move_string = ''
        #Add horizontal moves to sequence
        if x > 0:
            move_string += x*'>'
        else:
            move_string += abs(x)*'<'
        #Add vertical moves to sequence
        if y > 0:
            move_string += y*'^'
        else:
            move_string += abs(y)*'v'

        perms = set([''.join(p) for p in permutations(move_string)])
        perms = [perm for perm in perms if (not ((prev_button == '0') and (perm[0] == '<')) and not ((prev_button == 'A') and (perm[:2] == '<<')))]
        perms = [perm for perm in perms if not ((button == '0') and (perm[-1] == '>')) or not ((button == 'A') and (perm[-2:] == '>>'))]
        #Remove perms that go into gap
                      
        #Need to end direction with a push of A
        perms = [perm + 'A' for perm in perms]
        final_sequences = [prev_sequence + perm for perm in perms for prev_sequence in final_sequences]
        prev_button = button
    return final_sequences


def find_directional_sequence(code):
    '''Find the pattern for directions on the 2nd keypad'''
    keypad = {}
    keypad['<'] = 0
    keypad['v'] = 1
    keypad['>'] = 2
    keypad['^'] = 1 + 1j
    keypad['A'] = 2 + 1j

    prev_button = 'A'
    final_sequences = ['']
    for button in code:
        distance = keypad[button] - keypad[prev_button]
        x, y = int(distance.real), int(distance.imag)
        move_string = ''
        #Add horizontal moves to sequence
        if x > 0:
            move_string += x*'>'
        else:
            move_string += abs(x)*'<'
        #Add vertical moves to sequence
        if y > 0:
            move_string += y*'^'
        else:
            move_string +=  abs(y)*'v'

        perms = set([''.join(p) for p in permutations(move_string)])
        if len(perms) >= 2:
            perms = [perm for perm in perms if not (prev_button == '<' and perm[0] == '^')]
            perms = [perm for perm in perms if not (button == '<' and perm[-1] == 'v')]
            #Remove perms that go into gap

        #Need to end direction with a push of A
        perms = [perm + 'A' for perm in perms]
        final_sequences = [prev_sequence + perm for perm in perms for prev_sequence in final_sequences]
        prev_button = button
    return final_sequences

def main():
    s = get_input('input.txt')
    total = 0
    for code in s:
        numeric = int(code.replace('A', ''))
        directional_sequences = find_keypad_sequence(code)
        for robot in range(2):
            directional_sequences = list(map(find_directional_sequence, directional_sequences))
            directional_sequences = list(chain(*directional_sequences))
        #Find the shortest sequence
        complexity = len(min(directional_sequences, key=len))
        #print(min(directional_sequences, key=len))
        #print(complexity, numeric)
        total += complexity * numeric
    print(total)


main()
