#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    height = 103
    width = 101

    q1 = q2 = q3 = q4 = 0

    for robot in s:
        stats = robot.split(' ')
        p, v = stats[0].split(','), stats[1].split(',')
        x_pos, y_pos = int(p[0][2:]), int(p[1])
        x_vel, y_vel = int(v[0][2:]), int(v[1])

        final_x = (x_pos + 100 * x_vel) % width
        final_y = (y_pos + 100 * y_vel) % height

        if final_x < (width - 1)/2 and final_y < (height - 1)/2:
            q1 += 1
        elif final_x > (width - 1)/2 and final_y < (height - 1)/2:
            q2 += 1
        elif final_x < (width - 1)/2 and final_y > (height - 1)/2:
            q3 += 1
        elif final_x > (width - 1)/2 and final_y > (height - 1)/2:
            q4 += 1

    print(q1*q2*q3*q4)





main()
