#!/opt/anaconda3/bin/python
#Jake Feiler


import sys
STEPS = 26501365

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_occurences(offset_from_origin, length):
    '''Count the number of times a square is visited, given its offset from the origin'''
    global STEPS
    highest_number_of_occurences = 0

    distance_to_edge = STEPS - offset_from_origin
    #Pattern repeats every 2L in a row
    highest_number_of_occurences = 1 + (distance_to_edge // (2*length))
    # Arithmetic series: 1 + n * (n/2)
    #Shift down 2H to see row pattern repeat, but shorter by 2L (think diamond pattern/manhattan distance)
    total_occurences = int(0.5 * (highest_number_of_occurences * (highest_number_of_occurences + 1)))
    return total_occurences

def main():

    garden = get_input('input.txt')

    length, height = len(garden[0]), len(garden)
    for row_pos, row in enumerate(garden):
        for col_pos, plot  in enumerate(row):
            if plot == 'S':
                start_y, start_x = row_pos, col_pos
                break

    #Also look for any cells totally blocked off (# in all 4 directions)
    offlimit_cells = []
    for row_pos, row in enumerate(garden[:-1]):
        for col_pos, plot in enumerate(row[:-1]):
            if row_pos == 0 or col_pos == 0:
                continue
            if garden[row_pos - 1][col_pos] == '#' and garden[row_pos + 1][col_pos] == '#'\
            and garden[row_pos][col_pos - 1] == '#' and garden[row_pos][col_pos + 1] == '#':
                offlimit_cells.append((row_pos, col_pos))

    #Hopeful observation - without rocks, can freely reach a diamond the proper distance away
    #With rocks, only illegal spaces are the ones with rocks on them as final points - all others are reachable
    #Rationalization - need to combine proper vert and horiz movements to reach the diamond.
    #Most constraints are the ones with little variety, but there's no rocks in the starting column or row
    #Then, do a smart count to eliminate all interior spots with rocks

    spaces_reached = 0
    print(length, height)
    #print(26501365%131)


    ways_to_reach_towards_one_quad = [[0]*length for h in range(height)]

    #Count occupancy in bottom-right quadrant
    #Similarity will apply to other 4 quadrants
    for orig_row_pos, row in enumerate(garden):
        for orig_col_pos, plot in enumerate(row):
            #Readjust grid - origin S is in bottom left
            #-65 -64 .... -1 S 1 ..... 64 65
            #-> S 1 2 ........130
            #Order of using/not using : 1 3 5 .... 129 S 2 4 .... 128 130   1....
            #Every other row: S 2 4 ..... 130 1 3 5 ...... 129
            row_pos = (orig_row_pos - start_x) % length
            col_pos = (orig_col_pos - start_y) % height

            """
            if col_pos % 2 == 0:
                col_pos += height
            if row_pos % 2 == 0:
                row_pos += length
            """

            #If even distance, it can only be visited in the next repeating pattern
            offset_from_origin = row_pos + col_pos

            #Also track the repeats for the next one
            offset_from_origin_2 = offset_from_origin + height
            if offset_from_origin % 2 == 0:
                offset_from_origin += length
            else:
                offset_from_origin_2 += length

            #print(row_pos, col_pos, offset_from_origin, offset_from_origin_2)
            #print(count_occurences(offset_from_origin, length) , count_occurences(offset_from_origin_2, length))
            total_occurences = count_occurences(offset_from_origin, length) + count_occurences(offset_from_origin_2, length)
            ways_to_reach_towards_one_quad[orig_row_pos][orig_col_pos] = total_occurences


    #print(ways_to_reach_towards_one_quad)
    #Symmetry with (x,y), unless on center axis
    for row_pos, row in enumerate(garden):
        for col_pos, plot in enumerate(row):
            if plot == '#' or (row_pos, col_pos) in offlimit_cells:
                continue
            else:
                spaces_reached += ways_to_reach_towards_one_quad[row_pos][col_pos] + \
                ways_to_reach_towards_one_quad[length - 1 - row_pos][col_pos] + \
                ways_to_reach_towards_one_quad[length - 1 - row_pos][height - 1 - col_pos] + \
                ways_to_reach_towards_one_quad[row_pos][height - 1 - col_pos]


    #Double counting of vertical lines
    #One direction: (STEPS + 1)/2, 4 occurences
    print(spaces_reached - 2*(STEPS + 1))









main()
