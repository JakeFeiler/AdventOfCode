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
    width = len(s[0])*2

    robot_coords = 0 + 0*1j
    for row_pos, row in enumerate(s[:blank_row]):
        for col_pos, val in enumerate(row):
            x = col_pos*2
            y = height - 1 - row_pos

            if val in ['@', '.']:
                val_2 = '.'
            elif val == '#':
                val_2 = '#'
            else:
                val = '['
                val_2 = ']'
            warehouse[x + y*1j] = val
            warehouse[x + 1 + y*1j] = val_2
            if val == '@':
                robot_coords = x + y*1j
                warehouse[x + y*1j] = '.'

    moves = ''.join(s[blank_row+1:])
    move_map = {'^': 0 + 1j, 'v': 0 - 1j, '<': -1, '>': 1}

    for move in moves:
        direction = move_map[move]

        #Horizontal move will work similar to before, just need to relocate all boxes
        if direction.imag == 0:

            #How many squares in a row are boxes
            consec_boxes = 0

            found_end_of_boxes = False
            explore_coords = robot_coords
            #Keep counting boxes until blank or wall is encountered
            while not found_end_of_boxes:
                explore_coords += direction
                occupant = warehouse[explore_coords]
                #Could've counted 2 at a time to save
                if occupant not in ('[', ']'):
                    found_end_of_boxes = True
                else:
                    consec_boxes += 1

            #Wall comes before blank, do nothing
            if occupant == '#':
                continue
            else:
                while consec_boxes >= 0:
                    #Result ultimately looks same, except the first box would move to end
                    warehouse[robot_coords + (consec_boxes + 1)*direction] = warehouse[robot_coords + consec_boxes*direction]
                    consec_boxes -= 1
                robot_coords += direction


        #Vertical move - now things get complicated
        else:
            #Next_up_coords - look above/below these to find rocks to psh
            next_up_coords = [robot_coords]
            coords_to_push = []

            can_move = True
            while len(next_up_coords) > 0:
                next_row_of_rocks = []

                #The highest/lowest row of rocks to push, see if they push more or get blocked
                for pushing_square in next_up_coords:
                    pushed_space = warehouse[pushing_square + direction]
                    if pushed_space == '#':
                        #Can't push anything, a wall is blocking
                        can_move = False
                        break
                    elif pushed_space == '.':
                        continue
                    if pushed_space in ['[', ']']:
                        #Look to move this rock too (and it's neighbor), if not already set for pushing
                        if pushing_square + direction not in next_row_of_rocks:
                            next_row_of_rocks.append(pushing_square + direction)
                        if pushed_space == '[':
                            if pushing_square + direction + 1 not in next_row_of_rocks:
                                next_row_of_rocks.append(pushing_square + direction + 1)
                        else:
                            if pushing_square + direction - 1 not in next_row_of_rocks:
                                next_row_of_rocks.append(pushing_square + direction - 1)

                #Store the previous coordinates
                coords_to_push += next_up_coords
                #Everything we just found will get pushed up at some point
                next_up_coords = next_row_of_rocks


            if can_move:
                #Move the robot and all pushable boxes, furthest first
                for coords in coords_to_push[::-1]:
                    warehouse[coords + direction] = warehouse[coords]
                    warehouse[coords] = '.'
                robot_coords += direction


    gps_sum = 0
    for square in warehouse:
        if warehouse[square] == '[':
            x_coord = square.real
            y_coord = height - 1 - square.imag
            gps_sum += (100*y_coord + x_coord)
    print(int(gps_sum))



main()
