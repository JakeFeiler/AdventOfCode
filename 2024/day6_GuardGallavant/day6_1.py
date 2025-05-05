#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    position = []
    #Find the start, and set the complex map
    lab = {}
    for row_pos, row in enumerate(s):
        for col_pos, value in enumerate(row):
            lab[col_pos + 1j * (len(s) - 1 - row_pos)] = value
            if value == '^':
                position = col_pos + 1j * (len(s) - 1 - row_pos)
    #Use the set to track visited squares
    found_spots = set()
    #Start by going north -> right turn is multiplying direction by -i
    direction = 0 + 1j
    while True:
        found_spots.add(position)
        try:
            next_pos = position + direction
            if lab[next_pos] == '#':
                direction *= (0 - 1j)
            position += direction
        except:
            #Kill once off the map
            break
    print(len(found_spots))
        

    

    

    


main()
