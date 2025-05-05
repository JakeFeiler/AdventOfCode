#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    total_score = 0
    shape_to_point = {'X': 1, 'Y': 2, 'Z': 3}
    wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}

    for shapes in s:
        opponent, me = shapes.split(' ')
        total_score += shape_to_point[me]
        if ord(me) - ord(opponent) == 23:
            total_score += 3
        else:
            if opponent == wins[me]:
                total_score += 6

    print(total_score)




main()
