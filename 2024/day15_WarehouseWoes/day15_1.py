#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]


def main():
    s = get_input('input.txt')
    warehouse = {}

    blank_row = 0
    for row_pos, row in enumerate(s):
        if row == '':
            blank_row = row_pos
            break

    height = blank_row
    width = len(s[0])

    robot_coords = 0 + 0*1j
    for row_pos, row in enumerate(s[:blank_row]):
        for col_pos, val in enumerate(row):
            x = col_pos
            y = height - 1 - row_pos
            warehouse[x + y*1j] = val
            if val == '@':
                robot_coords = x + y*1j
                warehouse[x + y*1j] = '.'

    moves = ''.join(s[blank_row+1:])
    move_map = {'^': 0 + 1j, 'v': 0 - 1j, '<': -1, '>': 1}

    for move in moves:
        direction = move_map[move]

        #How many squares in a row are boxes
        consec_boxes = 0

        found_end_of_boxes = False
        explore_coords = robot_coords
        #Keep counting boxes until blank or wall is encountered
        while not found_end_of_boxes:
            explore_coords += direction
            occupant = warehouse[explore_coords]
            if occupant != 'O':
                found_end_of_boxes = True
            else:
                consec_boxes += 1

        #Wall comes before blank, do nothing
        if occupant == '#':
            continue
        else:
            #Result ultimately looks same, except the first box would move to end
            warehouse[robot_coords + (consec_boxes + 1)*direction] = 'O'
            warehouse[robot_coords + direction] = '.'
            robot_coords += direction
            
        
    gps_sum = 0
    for square in warehouse:
        if warehouse[square] == 'O':
            x_coord = square.real
            y_coord = height - 1 - square.imag
            gps_sum += (100*y_coord + x_coord)
    print(int(gps_sum))


main()
