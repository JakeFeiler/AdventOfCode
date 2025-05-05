#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

#I removed newlines from the input by hand, could've been done automatically in other ways

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    program = get_input('input.txt')[0]

    mul_results = 0

    next_mul_loc = program.find('mul(')
    
    while next_mul_loc >= 0:
        #Jump to the next mul (addition + 3 to jump to the end of the 'mul('
        program = program[next_mul_loc + 1 + 3:]
        try:
            #Attempt to split 2 numbers by a comma before the next )
            through_next_paren= program[:program.find(')')]
            if ' ' in through_next_paren:
                #Skip if spaces exist, which int() can tolerate
                raise
            value_1, value_2 = through_next_paren.split(',')
            mul_results += int(value_1) * int(value_2)
        except:
            pass

        next_mul_loc = program.find('mul(')
        
    print(mul_results)

main()

#24286181
#153469856
