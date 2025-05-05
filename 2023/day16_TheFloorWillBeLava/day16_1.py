#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    cave = get_input('input.txt')
    row_length = len(cave[0])
    col_length = len(cave)

    illuminated = [['' for _ in range(row_length)] for _ in range(col_length)]
    
    paths = [tuple([0, 0, 'R'])]

    forward_mapping = {'R': 'U', 'U': 'R', 'L': 'D', 'D': 'L'}
    backward_mapping = {'L': 'U', 'U': 'L', 'R': 'D', 'D': 'R'}

    while len(paths) != 0:
        beam_x, beam_y, beam_dir = paths.pop()
        while 0 <= beam_x < col_length and 0 <= beam_y < row_length:
            #Check if we've already visited this square, going this direction, break if so
            if beam_dir in illuminated[beam_y][beam_x]:
                beam_x = -1
                break
            else:
                illuminated[beam_y][beam_x] += beam_dir
            cave_sq = cave[beam_y][beam_x]
            if cave_sq == '/':
                beam_dir = forward_mapping[beam_dir]
            elif cave_sq == '\\':
                beam_dir = backward_mapping[beam_dir]
            elif cave_sq == '|' and beam_dir in ['L', 'R']:
                beam_dir = 'D'
                paths.append(tuple([beam_x, beam_y - 1, 'U']))
            elif cave_sq == '-' and beam_dir in ['U', 'D']:
                beam_dir = 'R'
                paths.append(tuple([beam_x - 1, beam_y, 'L']))

            if beam_dir == 'R':
                beam_x += 1
            elif beam_dir == 'L':
                beam_x -= 1
            elif beam_dir == 'D':
                beam_y += 1
            elif beam_dir == 'U':
                beam_y -= 1


    illuminated_squares = 0
    for row in illuminated:
        for square in row:
            if len(square) > 0:
                illuminated_squares += 1
    print(illuminated_squares)
main()
