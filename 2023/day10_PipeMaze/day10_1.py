#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def take_a_step(prev_move, current_coordinates, pipe_grid):
    '''Advance one spot based on location info'''
    curr_x, curr_y = current_coordinates[0], current_coordinates[1]
    curr_square = pipe_grid[curr_x][curr_y]

    if curr_square == '|':
        if prev_move == 'U':
            return 'U', [curr_x - 1, curr_y]
        else:
            return 'D', [curr_x + 1, curr_y]
    elif curr_square == '-':
        if prev_move == 'R':
            return 'R', [curr_x, curr_y + 1]
        else:
            return 'L', [curr_x, curr_y - 1]

    elif curr_square == '7' or curr_square == 'S':
        if prev_move == 'U':
            return 'L', [curr_x, curr_y - 1]
        else:
            return 'D', [curr_x + 1, curr_y]
    elif curr_square == 'F':
        if prev_move == 'U':
            return 'R', [curr_x, curr_y + 1]
        else:
            return 'D', [curr_x + 1, curr_y]
    elif curr_square == 'L':
        if prev_move == 'D':
            return 'R', [curr_x, curr_y + 1]
        else:
            return 'U', [curr_x - 1, curr_y]
    elif curr_square == 'J':
        if prev_move == 'D':
            return 'L', [curr_x, curr_y - 1]
        else:
            return 'U', [curr_x - 1, curr_y]



def main():
    pipe_grid = get_input('input.txt')
    for row_num, row in enumerate(pipe_grid):
        for col_num, pipe_square in enumerate(row):
            if pipe_square == 'S':
                starting_square = [row_num, col_num]
                break
    #inspection: S = 7
    #Inspect counterclockwise
    prev_move = 'U'
    current_square = starting_square
    made_a_move = False
    number_of_steps = 0
    while not made_a_move or current_square != starting_square:
        made_a_move = True
        prev_move, current_square = take_a_step(prev_move, current_square, pipe_grid)
        number_of_steps += 1
    furthest_point = number_of_steps//2
    print(furthest_point)







main()
