#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    
    highest_cal_count = 0
    current_cal_count = 0

    for calories in s:
        if calories != '':
            current_cal_count += int(calories)
        else:
            if current_cal_count > highest_cal_count:
                highest_cal_count = current_cal_count
            current_cal_count = 0

    #check one more time for EOF
    #if current_cal_count > highest_cal_count:
    #    highest_cal_count = current_cal_count

    print(highest_cal_count)

main()
