#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [int(line.strip().replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for line in input_file]

'''
def calc_seat_ID(boarding_pass):
    #Determine seat ID based off boarding pass
    row, seat = boarding_pass[:7], boarding_pass[7:]
    #print(row, seat)
    #print(int(row, 2) * int(seat, 2))
    return int(row, 2) * 8 + int(seat, 2)
'''

def main():
    #getting input converts seat numbers to binary
    passes = get_input('input.txt')
    min_value = 127 * 8 + 7
    max_value = 0
    sum_of_seats = 0
    for boarding_pass in passes:
        min_value = min(boarding_pass, min_value)
        max_value = max(boarding_pass, max_value)
        sum_of_seats += boarding_pass

    #Sum arithmetic series
    #Empty seat will be difference between sum of all seats and the series
    empty_seat = (min_value + max_value) * (max_value - min_value + 1)/2 - sum_of_seats
    print(int(empty_seat))


main()
