#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

#I removed newlines from the input by hand, could've been done automatically in other ways

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def determine_state(start_of_next_instruc, program, current_state):
    '''Return the status, based on where you're at in program'''
    next_on = program.rfind('do()', 0 , start_of_next_instruc)
    next_off = program.rfind("don't()", 0 , start_of_next_instruc)


    #Return previous state if no do's/don'ts
    if next_on < 0 and next_off < 0:
        return current_state
    elif next_on > next_off:
        return True
    return False


def main():
    program = get_input('input.txt')[0]

    mul_results = 0

    next_mul_loc = program.find('mul(')

    active = True
    
    while next_mul_loc >= 0:
        #Jump to the next mul (addition + 3 to jump to the end of the 'mul('
        active = determine_state(next_mul_loc, program, active)
        program = program[next_mul_loc + 1 + 3:]
        try:
            #Attempt to split 2 numbers by a comma before the next )
            through_next_paren= program[:program.find(')')]
            if ' ' in through_next_paren or not active:
                #Skip if spaces exist, which int() can tolerate
                raise
            value_1, value_2 = through_next_paren.split(',')
            mul_results += int(value_1) * int(value_2)
        except:
            pass

        next_mul_loc = program.find('mul(')
        
    print(mul_results)

main()
