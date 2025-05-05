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

def main():
    s = get_input('input.txt')
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0

    all_positions = {(0,0)}

    for command in s:
        direction, amount = command[0], int(command[2:])
        while amount > 0:
            amount -= 1
            head_x, head_y = move(head_x, head_y, direction)

            #Now check on tail
            #If <= 1 apart in both directions, move on
            if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
                continue
            #If same row or column, update that position
            elif head_x == tail_x:
                tail_y = int((tail_y + head_y)/2)
            elif head_y == tail_y:
                tail_x = int((tail_x + head_x)/2)
            else:
                #Diagonal apart
                #If move was North or South, x is the same
                if direction in ('U', 'D'):
                    tail_x = head_x
                    tail_y = int((tail_y + head_y)/2)
                else:
                    tail_y = head_y
                    tail_x = int((tail_x + head_x)/2)

            all_positions.add((tail_x, tail_y))

    print(len(all_positions))



main()
