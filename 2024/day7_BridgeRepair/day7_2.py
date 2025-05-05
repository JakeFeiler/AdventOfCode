#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def is_possibly_valid(result, factors, current_value):
    '''See if the remainder of the equation would work'''
    #If no more nummber to use, see if this works
    if len(factors) == 0:
        return result == current_value
    #Otherwise, see if the remainder will work with either a + or * or ||
    with_plus_next =  is_possibly_valid(result, factors[1:], current_value + factors[0])
    with_multiply_next =  is_possibly_valid(result, factors[1:], current_value * factors[0])
    #Concatenation - multiply by 10 to the <enough power to allow for addition of nuext value>
    #Done by taking ceiling of log function to count digits
    #Only issue: 1 -> 0. Solve by adding 0.1 to everything
    with_concat_next =  is_possibly_valid(result, factors[1:], current_value*(10**math.ceil(math.log(factors[0] + 0.1, 10))) + factors[0])
    return with_plus_next or with_multiply_next or with_concat_next
    
    
    
def main():
    s = get_input('input.txt')
    calibration_result = 0
    for eq in s:
        values = eq.split(' ')
        result = int(values[0][:-1])
        starting_value = int(values[1])
        factors = list(map(int, values[1:]))
        if is_possibly_valid(result, factors[1:], starting_value):
            calibration_result += result
    print(calibration_result)

main()
