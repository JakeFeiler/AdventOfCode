#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def calc_seat_ID(boarding_pass):
    '''Determine seat ID based off boarding pass'''
    row, seat = boarding_pass[:7], boarding_pass[7:]
    #print(row, seat)
    #print(int(row, 2) * int(seat, 2))
    return int(row, 2) * 8 + int(seat, 2)

def main():
    passes = get_input('input.txt')
    max_seat_id = 0
    for boarding_pass in passes:
        bp = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        max_seat_id = max(max_seat_id, calc_seat_ID(bp))
    print(max_seat_id)

main()
