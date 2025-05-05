#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    final_value = 0

    for game_text in s:
        game = game_text.split(':')[1]

        max_possible = {'red': 0, 'green': 0, 'blue': 0}

        sets = game.split('; ')
        for indiv_set in sets:
            cube_sections = indiv_set.strip().split(', ')
            for section in cube_sections:
                [number, color] = section.split(' ')
                number = int(number)
                max_possible[color] = max(max_possible[color], number)

        final_value += max_possible['red'] * max_possible['green'] * max_possible['blue']

    print(final_value)

main()
