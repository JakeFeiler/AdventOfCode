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
        min_count, max_count = int(values[0]), int(values[1])
        target = ps[1][0]
        letter_count = 0
        for letter in ps[2]:
            if letter == target:
                letter_count += 1
        if min_count <= letter_count <= max_count:
            valid_passwords += 1

    print(valid_passwords)

main()
