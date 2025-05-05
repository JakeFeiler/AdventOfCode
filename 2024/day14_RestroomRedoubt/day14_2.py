#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import matplotlib.pyplot as plt

HEIGHT = 103
WIDTH = 101

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

class robot:
    '''Qualities of the robot'''
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self):
        global HEIGHT
        global WIDTH
        self.x_pos = (self.x_pos + self.x_vel) % WIDTH
        self.y_pos = (self.y_pos + self.y_vel) % HEIGHT

    def get_coords(self):
        return (self.x_pos, self.y_pos)

def main():
    s = get_input('input.txt')



    robots = []

    for robot_stats in s:
        stats = robot_stats.split(' ')
        p, v = stats[0].split(','), stats[1].split(',')
        x_pos, y_pos = int(p[0][2:]), int(p[1])
        x_vel, y_vel = int(v[0][2:]), int(v[1])

        robots.append(robot(x_pos, y_pos, x_vel, y_vel))

    seconds = 0
    while True:
        robot_x_coords = []
        robot_y_coords = []
        for robby in robots:
            coords = robby.get_coords()
            robot_x_coords.append(coords[0])
            robot_y_coords.append(HEIGHT - 1 - coords[1]) 
        #While testing - interesting pattern every 71 + 101k
        #Presumably also a pattern involving the width at an interval of 103, just going to brute force above to find patttern
        if (seconds - 71) % 101 == 0:
            plt.scatter(robot_x_coords, robot_y_coords)
            plt.title(str(seconds))
            plt.show()
        seconds += 1
        for robby in robots:
            robby.move()

    #Pattern found at 71 + 101*79 = 8050



main()
