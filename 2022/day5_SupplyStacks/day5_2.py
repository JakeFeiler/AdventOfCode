#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from queue import LifoQueue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    #not stripping to handle whitespace in initial crates
    return [line for line in input_file]

def main():
    s = get_input('input.txt')
    stacks = []
    temp_stacks = []
    #input read backwards, pop these temporary stacks to make actual ones
    
    #9 stacks in input
    for i in range(9):
        stacks.append(LifoQueue())
        temp_stacks.append(LifoQueue())

    finished_with_setup = False

    for row in s:
        #to handle newline separator
        if row == '\n':
            pass

        #Time to stop setting up, prepare for moving
        elif row[1] == '1':
            finished_with_setup = True
            #reverse temp_stacks into stacks
            for position, temp_stack in enumerate(temp_stacks):
                while not temp_stack.empty():
                    stacks[position].put(temp_stack.get())

        #Still on set-up phase, build up the stacks
        elif not finished_with_setup:
            for x in range(9):
                crate = row[4*x + 1]
                if crate != ' ':
                    temp_stacks[x].put(crate)

        else:
            row = row.split(' ')
            amount, dest, target = int(row[1]), int(row[3]), int(row[5])
            #We'll reverse the stack as we pull using a temp stack
            temp_moving_stack = LifoQueue()
            while amount > 0:
                temp_moving_stack.put(stacks[dest - 1].get())
                amount -= 1
            while not temp_moving_stack.empty():
                stacks[target - 1].put(temp_moving_stack.get())


    final_string = ''
    for stack in stacks:
        final_string += stack.get()
    print(final_string)

main()


