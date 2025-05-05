#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]
        
def main():
    password_sets = get_input('input.txt')
    valid_passwords = 0
    for password_set in password_sets:
        ps = password_set.split(' ')
        values = ps[0].split('-')
        first_spot, second_spot = int(values[0]), int(values[1])
        target = ps[1][0]
        valid_passwords += (ps[2][first_spot - 1] == target) ^ (ps[2][second_spot - 1] == target)

    print(valid_passwords)

main()
