#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
CAVE = ""
ROW_LENGTH = 0
COL_LENGTH = 0



def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_illuminated_squares(start_x, start_y, start_dir):
    '''Determine how many squares will get lit up from this starting point'''

    global CAVE
    global ROW_LENGTH
    global COL_LENGTH

    paths = [tuple([start_x, start_y, start_dir])]

    illuminated = [['' for _ in range(ROW_LENGTH)] for _ in range(COL_LENGTH)]


    forward_mapping = {'R': 'U', 'U': 'R', 'L': 'D', 'D': 'L'}
    backward_mapping = {'L': 'U', 'U': 'L', 'R': 'D', 'D': 'R'}

    while len(paths) != 0:
        beam_x, beam_y, beam_dir = paths.pop()
        while 0 <= beam_x < COL_LENGTH and 0 <= beam_y < ROW_LENGTH:
            #Check if we've already visited this square, going this direction, break if so
            if beam_dir in illuminated[beam_y][beam_x]:
                beam_x = -1
                break
            else:
                illuminated[beam_y][beam_x] += beam_dir
            cave_sq = CAVE[beam_y][beam_x]
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

    return illuminated_squares

def main():
    global CAVE, ROW_LENGTH, COL_LENGTH
    CAVE = get_input('input.txt')
    ROW_LENGTH = len(CAVE[0])
    COL_LENGTH = len(CAVE)



    max_illumination = 0
    for i in range(COL_LENGTH):
        max_illumination = max(max_illumination, count_illuminated_squares(0, i, 'R'))
        max_illumination = max(max_illumination, count_illuminated_squares(ROW_LENGTH - 1, i, 'L'))

    for j in range(ROW_LENGTH):
        max_illumination = max(max_illumination, count_illuminated_squares(j, 0, 'D'))
        max_illumination = max(max_illumination, count_illuminated_squares(j, COL_LENGTH - 1, 'U'))
        


    print(max_illumination)
main()
