#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    vertices = []
    x_coord, y_coord = 0, 0
    ext_points = 0
    for dig_path in s:
        dig_path = dig_path.split(' ')
        direction, count = dig_path[0], int(dig_path[1])
        if direction == 'L':
            x_coord -= count
        elif direction == 'R':
            x_coord += count
        elif direction == 'U':
            y_coord += count
        elif direction == 'D':
            y_coord -= count
        ext_points += count
        vertices.append((x_coord, y_coord))

    #Tracked the count of exterior integer points already (E)
    #To find interior points (I), combine Shoelace Formula with Pick's theorem
    #2A = det(v1,v2) = det(v2,v3) + ... + det(vn, v1)
    #A = I + E/2 - 1 -> A + 1 - E/2 = I

    #desired answer = I + E

    shifted_vertices = vertices[1:]
    shifted_vertices.append(vertices[0])

    area = 0
    #Shoelace
    for v in range(len(vertices)):
        area += vertices[v][0]*shifted_vertices[v][1] - vertices[v][1]*shifted_vertices[v][0]
    area /= 2

    #*-1, as perimter is benig tracked clockwise, so negatve orientation
    area *= -1

    #Pick
    int_points = int(area) + 1 - ext_points//2

    print(int_points + ext_points)


main()
