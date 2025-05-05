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

    elif curr_square == '7':
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

    loop_occupants = [[0] * len(pipe_grid[0])] * len(pipe_grid)
    loop_occupants = [[0 for a in range(len(pipe_grid[0]))] for b in range(len(pipe_grid))]

    for row_num, row in enumerate(pipe_grid):
        for col_num, pipe_square in enumerate(row):
            if pipe_square == 'S':
                #Found by inspection
                pipe_grid[row_num] = pipe_grid[row_num].replace('S', '7')
                starting_square = [row_num, col_num]
                break



    #inspection: S = 7
    #Inspect counterclockwise
    prev_move = 'U'
    current_square = starting_square
    made_a_move = False
    while not made_a_move or current_square != starting_square:
        curr_x, curr_y = current_square[0], current_square[1]
        loop_occupants[curr_x][curr_y] = 1
        made_a_move = True
        prev_move, current_square = take_a_step(prev_move, current_square, pipe_grid)



    #Idea - every vertical bar separates IN from OUT
    # | is flip, L7, FJ are as well
    #LJ & F7 will NOT flip

    pieces_in_loop = 0
    prev_found_piece = ''
    prev_flipping = {'L': '7', '7': 'L', 'F': 'J', 'J': 'F'}

    for row_pos, row in enumerate(loop_occupants):
        inside_loop = False
        for col_pos, piece in enumerate(row):
            pipe_grid_piece = pipe_grid[row_pos][col_pos]
            if piece == 0 and inside_loop:
                pieces_in_loop += 1
            elif piece == 1:
                if pipe_grid_piece == '|':
                    inside_loop = not inside_loop
                    prev_found_piece = ''

                #FJL7
                if pipe_grid_piece in prev_flipping:
                    if prev_found_piece == '':
                        prev_found_piece = pipe_grid_piece
                    else:
                        if prev_found_piece == prev_flipping[pipe_grid_piece]:
                            inside_loop = not inside_loop              
                        prev_found_piece = ''





    print(pieces_in_loop)

    #loop occupants grid
    #Rows will alternate between 'in' and 'out' as vertical bars are found







main()
