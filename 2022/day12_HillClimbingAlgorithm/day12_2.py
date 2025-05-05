#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

#Use the A* algorithm


def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def calculate_manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def determine_min_distance(start, end, hill, max_rows, max_columns):
    '''From starting point 'start', determine the minimum steps needed using A*'''

    initial_distance = calculate_manhattan_distance(start, end)
    unexplored = {start: initial_distance}
    explored = {}
    #2 lists - unexplored tracks unexplored routes (or explored with better heuristic)
    #explored tracks best way to get to a point

    while len(unexplored) > 0:
        best_coordinate = (0, 0)
        best_value = 100000
        for coordinate in unexplored:
            if unexplored[coordinate] < best_value:
                best_coordinate = coordinate
                best_value = unexplored[coordinate]

        #Taking the best value of h
        #h = f + g
        #f = steps taken from start
        #g = minimum possible steps to get to end, ignoring terrain

        z = unexplored.pop(best_coordinate)
        x, y = best_coordinate[0], best_coordinate[1]
        current_height = hill[x][y]
        successors = []

        #Need to separate heuristic in order to increment f
        prev_manhattan = calculate_manhattan_distance((x, y), end)
        steps_so_far = best_value - prev_manhattan

        #If this is the goal, print the steps needed (g=0), and end the program
        if prev_manhattan == 0:
            return best_value

        #Consider all in-bounds successors
        if x != 0:
            successors.append(((x - 1, y), (1 + steps_so_far) + calculate_manhattan_distance((x - 1, y), end)))
        if x != max_rows - 1:
            successors.append(((x + 1, y), (1 + steps_so_far) + calculate_manhattan_distance((x + 1, y), end)))
        if y != 0:
            successors.append(((x, y - 1), (1 + steps_so_far) + calculate_manhattan_distance((x, y - 1), end)))
        if y != max_columns - 1:
            successors.append(((x, y + 1), (1 + steps_so_far) + calculate_manhattan_distance((x, y + 1), end)))

        for successor in successors:
            new_coord, heuristic = successor[0], successor[1]
            #print(new_coord[0], new_coord[1])
            successor_height = hill[new_coord[0]][new_coord[1]]
            #Skip if can't reach this next point (too high)
            if successor_height > (current_height + 1):
                continue
            #Skip if already planning on exploring this spot with a better heuristic
            if new_coord in unexplored:
                if heuristic > unexplored[new_coord]:
                    continue
            #Skip if already reached this spot with a better heuristic
            if new_coord in explored:
                if heuristic > explored[new_coord]:
                    continue
            #Otherwise, it's a new spot to explore, mark the old spot as previously explored
            unexplored[new_coord] = heuristic
            explored[best_coordinate] = best_value
    #Couldn't find a way, return a failure
    return -1




def main():
    s = get_input('input.txt')
    max_columns = len(s[0])
    max_rows = len(s)
    hill = [[0 for y in range(max_columns)] for x in range(max_rows)]
    #lots of possible starts
    starts = []
    end = (0, 0)

    #parse input: a=1, z=26
    for row_num, row in enumerate(s):
        for col_num, height in enumerate(row):
            if height in ('S', 'a'):
                #These could all be starting positions
                height_num = 1
                starts.append((row_num, col_num))
            elif height == 'E':
                height_num = 26
                end = (row_num, col_num)
            else:
                height_num = ord(height) - 96
            hill[row_num][col_num] = height_num

    #Check all starts
    fewest_steps = -1
    for start in starts:
        steps_this_way = determine_min_distance(start, end, hill, max_rows, max_columns)
        if (steps_this_way < fewest_steps and steps_this_way >= 0) or fewest_steps < 0:
            fewest_steps = steps_this_way
    print(fewest_steps)






main()
