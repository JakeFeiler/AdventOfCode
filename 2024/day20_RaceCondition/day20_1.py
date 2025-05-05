#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def run_through_maze(maze, start, end, direction):
    """Find the order of squares in the maze"""
    #Direction hard-coded based on input

    maze_path = [start]
    location = start
    while location != end:
        for rot in [1j, 1, -1j]:
            if maze[location + direction*rot] == '.':
                maze_path.append(location)
                direction *= rot
                location += direction
                break
    #Add in the end
    maze_path.append(location)
    return maze_path

def count_time_saved(maze, maze_path, wall_coord):
    '''if wall_coord was removed, how much time was saved'''
    #Time saved is difference between squares on the path, + 2 for time it takes to move through
    #Check if we can move horizontally or vertically through the wall
    #Horizontal
    if maze[wall_coord - 1] == '.' and maze[wall_coord + 1] == '.':
        return abs(maze_path.index(wall_coord -1) - maze_path.index(wall_coord + 1)) - 2
    #Vertical
    elif maze[wall_coord - 1j] == '.' and maze[wall_coord + 1j] == '.':
        return abs(maze_path.index(wall_coord -1j) - maze_path.index(wall_coord + 1j)) - 2
    #Not possible otherwise
    else:
        return 0

def main():
    s = get_input('input.txt')
    maze = {}
    wall_coords = []
    width, height = len(s[0]), len(s)
    for row_pos, row in enumerate(s):
        for col_pos, val in enumerate(row):
            coords = col_pos + row_pos*1j
            if val == 'S':
                start = coords
                val = '.'
            elif val == 'E':
                end = coords
                val = '.'
            #Track all walls for replacement (but can ignore edges)
            elif val == '#' and 0 < coords.real < width - 1 and 0 < coords.imag < height - 1:
                wall_coords.append(coords)
            maze[coords] = val

    #Order of steps needed to get through path
    maze_path = run_through_maze(maze, start, end, 1j)

    super_savers = 0
    for wall_coord in wall_coords:
        time_saved = count_time_saved(maze, maze_path, wall_coord)
        if time_saved >= 100:
            super_savers += 1
    print(super_savers)


main()
