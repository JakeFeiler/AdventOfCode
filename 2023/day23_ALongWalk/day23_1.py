#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

sys.setrecursionlimit(10000)

LENGTH = 0
HEIGHT = 0
S = []

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_path(curr_x, curr_y, distance_traveled_so_far, visited_squares):
    '''Find the path from here to the finish'''
    global LENGTH, HEIGHT, S
    worst_path = distance_traveled_so_far
    if curr_x == HEIGHT - 1:
        return worst_path
    down_square = S[curr_x + 1][curr_y]
    up_square = S[curr_x - 1][curr_y]
    left_square = S[curr_x][curr_y - 1]
    right_square = S[curr_x][curr_y + 1]




    #If the adjacent square is a steep slope, force the next 2 steps
    if down_square == '.' and (curr_x + 1, curr_y) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.add((curr_x + 1, curr_y))
        worst_path = max(worst_path, count_path(curr_x + 1, curr_y, distance_traveled_so_far + 1, new_visits))
    elif down_square == 'v' and (curr_x + 1, curr_y) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.update([(curr_x + 1, curr_y), (curr_x + 2, curr_y)])
        worst_path = max(worst_path, count_path(curr_x + 2, curr_y, distance_traveled_so_far + 2, new_visits))

    if up_square == '.' and (curr_x - 1, curr_y) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.add((curr_x - 1, curr_y))
        worst_path = max(worst_path, count_path(curr_x - 1, curr_y, distance_traveled_so_far + 1, new_visits))
    elif up_square == '^' and (curr_x - 1, curr_y) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.update([(curr_x - 1, curr_y), (curr_x - 2, curr_y)])
        worst_path = max(worst_path, count_path(curr_x - 2, curr_y, distance_traveled_so_far + 2, new_visits))

    if right_square == '.' and (curr_x, curr_y + 1) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.add((curr_x, curr_y + 1))
        worst_path = max(worst_path, count_path(curr_x, curr_y + 1, distance_traveled_so_far + 1, new_visits))
    elif right_square == '>' and (curr_x, curr_y + 1) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.update([(curr_x, curr_y + 1), (curr_x, curr_y + 2)])
        worst_path = max(worst_path, count_path(curr_x, curr_y + 2, distance_traveled_so_far + 2, new_visits))

    if left_square == '.' and (curr_x, curr_y - 1) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.add((curr_x, curr_y - 1))
        worst_path = max(worst_path, count_path(curr_x, curr_y - 1, distance_traveled_so_far + 1, new_visits))
    elif left_square == '<' and (curr_x, curr_y - 1) not in visited_squares:
        new_visits = visited_squares.copy()
        new_visits.update([(curr_x, curr_y - 1), (curr_x, curr_y - 2)])
        worst_path = max(worst_path, count_path(curr_x, curr_y - 2, distance_traveled_so_far + 2, new_visits))


    return worst_path


def main():
    global S
    S = get_input('input.txt')
    global LENGTH
    LENGTH = len(S[0])
    global HEIGHT
    HEIGHT = len(S)

    #inspection - force at (1,1)
    worst_path = count_path(1, 1, 1, {(0,1), (1,1)})
    print(worst_path)


main()
