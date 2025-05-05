#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    total = 0

    for cal_value in s:
        for char in cal_value:
            if char.isdigit():
                total += 10*int(char)
                break
        for char in cal_value[::-1]:
            if char.isdigit():
                total += int(char)
                break


    print(total)


main()
