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

    game_number = 0
    for game_text in s:
        game_number += 1
        game = game_text.split(':')[1]

        is_possible_game = True

        sets = game.split('; ')
        for indiv_set in sets:
            cube_sections = indiv_set.strip().split(', ')
            for section in cube_sections:
                [number, color] = section.split(' ')
                number = int(number)
                if (color == 'red' and number > 12) \
                or (color == 'green' and number > 13) \
                or (color == 'blue' and number > 14):
                    is_possible_game = False

        if is_possible_game:
            final_value += game_number

    print(final_value)

main()
