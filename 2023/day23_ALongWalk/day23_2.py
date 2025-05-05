#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

LENGTH = 0
HEIGHT = 0
S = []

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

class segment():
    #Rather than map every point, memorize the segments connecting intersections
    def __init(self, x_1, x_2, y_1, y_2, length, connections):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.length = length
        self.connections = connections

    def add_connectiion(new_x_1, new_x_2, new_y_1, new_y_2):
        self.connections.append((new_x_1, new_x_2, new_y_1, new_y_2))

def find_segments(grid):
    '''Create map of all intersections'''
    segments = ()
    global LENGTH, HEIGHT
    connections = dd(list)

    #Find endpoints, anythng that has an option of where to go next (or start & end)
    endpoints = [(0,1), ((HEIGHT - 1), (LENGTH -2))]
    for row_pos, row in enumerate(grid[1:-1]):
        for col_pos in range(1, LENGTH - 1):
            down_square = S[row_pos + 1][col_pos]
            up_square = S[row_pos - 1][col_pos]
            left_square = S[row_pos][col_pos - 1]
            right_square = S[row_pos][col_pos + 1]
            is_intersection = int(down_square == 'v') + int(up_square == 'v') + int(left_square == '>') + int(right_square == '>') >= 2
            if is_intersection:
                endpoints.append((row_pos, col_pos))

    #For every endpoint, determine its options of both the next endpoint and how many steps to reach the endpoint
    for row_pos, row in enumerate(grid[1:-1]):
        for col_pos in range(1, LENGTH - 1):
            if (row_pos, col_pos) in endpoints:

                down_square = S[row_pos + 1][col_pos]
                up_square = S[row_pos - 1][col_pos]
                left_square = S[row_pos][col_pos - 1]
                right_square = S[row_pos][col_pos + 1]

                #Should be functioned
                if down_square == 'v' or row_pos == 0:
                    seg_details = add_segment(row_pos, col_pos, (1,0), endpoints)
                    start_x, start_y, end_x, end_y, length = seg_details
                    connections[(start_x, start_y)].append((end_x, end_y, length))
                if up_square == 'v':
                    seg_details = add_segment(row_pos, col_pos, (-1,0), endpoints)
                    start_x, start_y, end_x, end_y, length = seg_details
                    connections[(start_x, start_y)].append((end_x, end_y, length))
                if left_square == '>':
                    seg_details = add_segment(row_pos, col_pos, (0,-1), endpoints)
                    start_x, start_y, end_x, end_y, length = seg_details
                    connections[(start_x, start_y)].append((end_x, end_y, length))
                if right_square == '>':
                    seg_details = add_segment(row_pos, col_pos, (0,1), endpoints)
                    start_x, start_y, end_x, end_y, length = seg_details
                    connections[(start_x, start_y)].append((end_x, end_y, length))

    return connections

def add_segment(start_x, start_y, direction, endpoints):
    '''Find all segments, what they connect to'''
    global S, HEIGHT
    squares_visited = set([(start_x, start_y)])
    curr_x = start_x + direction[0]
    curr_y = start_y + direction[1]

    #Map out the start to the end
    found_endpoint = False
    while not found_endpoint:
        #print(start_x, start_y, curr_x, curr_y)
        squares_visited.add((curr_x, curr_y))

        if (curr_x, curr_y) in endpoints:
            found_endpoint = True
            break


        down_square = S[curr_x + 1][curr_y]
        can_go_down = (down_square != '#' and (curr_x + 1, curr_y) not in squares_visited)
        if can_go_down:
            curr_x +=1
            continue

        up_square = S[curr_x - 1][curr_y]
        can_go_up = (up_square != '#' and (curr_x - 1, curr_y) not in squares_visited)
        if can_go_up:
            curr_x -= 1
            continue

        left_square = S[curr_x][curr_y - 1]
        can_go_left = (left_square != '#' and (curr_x, curr_y - 1) not in squares_visited)
        if can_go_left:
            curr_y -= 1
            continue

        right_square = S[curr_x][curr_y + 1]
        can_go_right = (right_square != '#' and (curr_x, curr_y + 1) not in squares_visited)
        if can_go_right:
            curr_y += 1
            continue


    return(start_x, start_y, curr_x, curr_y, len(squares_visited) - 1)


def find_worst_path(connections, curr_steps, current_point, used_points):
    '''Find the path to the finish'''

    global HEIGHT
    used_points.append(current_point)
    #print(current_point, used_points)

    #Return this distance if at bottom
    if current_point[0] == HEIGHT - 1:
        return curr_steps

    #All off the connected endpoints
    next_points_to_visit = connections[current_point]
    next_option_distances = []

    #Try exploring all coonnections if so far not used
    for next_point_to_visit in next_points_to_visit:
        next_x, next_y, distance_to_next = next_point_to_visit
        #print(current_point, next_point_to_visit, len(used_points), curr_steps)
        if (next_x, next_y) not in used_points:
            #print('\t',current_point, next_point_to_visit)
            next_option_distances.append(find_worst_path(connections, curr_steps + distance_to_next, (next_x, next_y), used_points.copy()))


    #If not at end and there are no more untrodden paths:
    if len(next_option_distances) == 0:
        return 0
    else:
        return max(next_option_distances)



def main():
    global S
    S = get_input('input.txt')
    global LENGTH
    LENGTH = len(S[0])
    global HEIGHT
    HEIGHT = len(S)

    connections = find_segments(S)

    current_point = (0,1)
    used_points = []
    worst_path_length = find_worst_path(connections, 0, current_point, used_points)

    print(worst_path_length)


main()
