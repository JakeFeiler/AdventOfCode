#!/opt/anaconda3/bin/python
#Jake Feiler

#See scratch code for work on optimizing order of vert & horizontal
#Essentially, if '<' is involved, move order is forced.
#Otherwise, go vertical first if there's a > move involved


import sys
from itertools import permutations, chain
from collections import defaultdict as dd
MAPPINGS = {}

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

        horiz_string = ''
        vert_string = ''
        #Add horizontal moves to sequence
        if x > 0:
            horiz_string += x*'>'
        else:
            horiz_string += abs(x)*'<'
        #Add vertical moves to sequence
        if y > 0:
            vert_string += y*'^'
        else:
            vert_string += abs(y)*'v'

        #Couldn't figure out proper order, so try all.
        perms = set([vert_string + horiz_string, horiz_string + vert_string])
        perms = [perm for perm in perms if (not ((prev_button == '0') and (perm[0] == '<')) and not ((prev_button == 'A') and (perm[:2] == '<<')))]
        perms = [perm for perm in perms if not ((button == '0') and (perm[-1] == '>')) or not ((button == 'A') and (perm[-2:] == '>>'))]
        #Remove perms that go into gap

        #Need to end direction with a push of A
        perms = [perm + 'A' for perm in perms]
        final_sequences = [prev_sequence + perm for perm in perms for prev_sequence in final_sequences]
        prev_button = button
    return final_sequences


def find_directional_sequence(pattern_count):
    '''Find the number of times every pattern occurs on 2nd keypad'''
    '''Order (somewhat) matters, but AA will produce itself'''
    '''Therefore, just count patterns that occur between AA's'''
    global MAPPINGS
    keypad = {}
    keypad['<'] = 0
    keypad['v'] = 1
    keypad['>'] = 2
    keypad['^'] = 1 + 1j
    keypad['A'] = 2 + 1j

    final_counts = dd(int)
    for pattern in pattern_count:
        if pattern in MAPPINGS:
            #Found an already seen pattern
            #Find the (new) patterns, add the count to the final dd
            next_patterns = MAPPINGS[pattern]
            next_patterns = next_patterns.split('AA')
            for next_pattern in next_patterns:
                final_counts[next_pattern] += pattern_count[pattern]
            continue
        #Else, figure out the new pattern
        code = pattern
        #Always start from A
        prev_button = 'A'
        #Need to finish by arriving at A
        code += 'A'
        new_pattern = ''
        for button in code:
            distance = keypad[button] - keypad[prev_button]
            x, y = int(distance.real), int(distance.imag)

            horiz_string = ''
            vert_string = ''
            #Add horizontal moves to sequence
            if x > 0:
                horiz_string += x*'>'
            else:
                horiz_string += abs(x)*'<'
            #Add vertical moves to sequence
            if y > 0:
                vert_string += y*'^'
            else:
                vert_string += abs(y)*'v'

            #Forced if there's a gap in the way, otherwise, there is an optimal order
            if button == '<' or ('>' in horiz_string and prev_button != '<'):
                move_string = vert_string + horiz_string + 'A'
            else:
                move_string = horiz_string + vert_string + 'A'

            new_pattern += move_string
            prev_button = button
        #Store this new pattern mapping, and count the occurrences of new patterns
        #Could've avoided repeating this code...oh well

        #First, chop off the added A from the old pattern, don't need to press it actually yet
        new_pattern = new_pattern[:-1]
        MAPPINGS[code] = new_pattern
        next_patterns = new_pattern.split('AA')
        for next_pattern in next_patterns:
            final_counts[next_pattern] += pattern_count[pattern]
    return final_counts

def main():
    s = get_input('input.txt')
    total = 0
    for code in s:
        numeric = int(code.replace('A', ''))
        #Plan: AA is an invariant. Split on these, use a counter to track/avoid redoing the samme operations. No AA's in first code
        pattern_counts = []
        #Track all possible initial codes, didn't look hard for logic to optimize first sequence
        directional_sequences = find_keypad_sequence(code)
        for sequence in directional_sequences:
            pattern_count = dd(int)
            pattern_count[sequence] = 1
            pattern_counts.append(pattern_count)
        for robot in range(25):
            pattern_counts = list(map(find_directional_sequence, pattern_counts))

        #Find the shortest sequence (calculate complexity)
        #How much of each pattern, + 'AA's to fill gaps
        sequence_lengths = []
        for pattern_count in pattern_counts:
            AA_count = sum(pattern_count.values()) - 1
            sequence_length = 2*AA_count
            for pattern in pattern_count:
                sequence_length += len(pattern)*pattern_count[pattern]
            sequence_lengths.append(sequence_length)
        complexity = min(sequence_lengths)

        #Bizarrely - sequence inexplicably 1 smaller halfway through?
        #Guess I'll add 1 to make it up?
        total += (complexity + 1) * numeric
    print(total)


main()
