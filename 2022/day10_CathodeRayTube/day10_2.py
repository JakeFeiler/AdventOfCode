#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    #middle of sprite is register
    register = 1
    cycle = 1

    screen = [['.' for i in range(40)] for j in range(6)]
    
    for instruction in s:
        
        #print(cycle, register)
        if abs(register%40 - (cycle - 1)%40) <= 1:
            screen[(cycle - 1)//40][(cycle)%40] = '#'

        cycle += 1

        if instruction == 'noop':
            pass
        else:
            #it's an addx #
            #for addx, add one extra cycle and redraw
            #print(cycle, register)
            if abs(register%40 - (cycle - 1)%40) <= 1:
                screen[(cycle - 1)//40][(cycle)%40] = '#'
            register_change = int(instruction.split(' ')[1])
            register += register_change
            cycle += 1




    for row in screen:
        print(*row, sep = '')



main()
