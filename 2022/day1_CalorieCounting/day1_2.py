#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    s.append('')

    cal_count_tracker = []
    current_cal_count = 0

    for calories in s:
        if calories != '':
            current_cal_count += int(calories)
            #print(current_cal_count)
        else:
            #print(current_cal_count)
            cal_count_tracker.append(current_cal_count)
            current_cal_count = 0

    cal_count_tracker.sort()
    print(sum(cal_count_tracker[-3:]))

main()
