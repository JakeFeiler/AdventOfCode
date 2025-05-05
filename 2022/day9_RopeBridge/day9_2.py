#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def move(x, y, direction):
    if direction == 'U':
        return (x, y + 1)
    elif direction == 'D':
        return (x, y - 1)
    elif direction == 'L':
        return (x - 1, y)
    else:
        return (x + 1, y)

def update_knot(head_x, head_y, tail_x, tail_y):
    '''Update the second knot to follow the first'''
    #Now check on tail
    #If <= 1 apart in both directions, move on
    x_diff = abs(head_x - tail_x)
    y_diff = abs(head_y - tail_y)

    if x_diff <= 1 and y_diff <= 1:
        return tail_x, tail_y


    #If same row or column, update that position

    elif x_diff == 0:   
        tail_y = int((tail_y + head_y)/2)
    elif y_diff == 0:
        tail_x = int((tail_x + head_x)/2)

    #2 away, jump diagonal
    elif x_diff == 2 and y_diff == 2:
        tail_y = int((tail_y + head_y)/2)
        tail_x = int((tail_x + head_x)/2)

    #knight move away, jump diagonal
    else:
        if x_diff == 1:
            tail_x = head_x
            tail_y = int((tail_y + head_y)/2)
        else:
            tail_y = head_y
            tail_x = int((tail_x + head_x)/2)

    return tail_x, tail_y

def main():
    s = get_input('input.txt')
    x_coords = [0 for i in range(10)]
    y_coords = [0 for i in range(10)]

    all_positions = {(0,0)}

    for command in s:
        direction, amount = command[0], int(command[2:])
        while amount > 0:
            amount -= 1
            x_coords[0], y_coords[0] = move(x_coords[0], y_coords[0], direction)

            for i in range(1,10):
                x_coords[i], y_coords[i] = update_knot(x_coords[i - 1], y_coords[i - 1], x_coords[i], y_coords[i])

            all_positions.add((x_coords[9], y_coords[9]))

    print(len(all_positions))

main()
