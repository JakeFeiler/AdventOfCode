#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input'''
    input_file = open(text, 'r')
    return input_file.read().split('\n\n')

def is_valid(passport):
    '''Return 1 if passport contains needed fields'''
    needed_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for field in needed_fields:
        if field not in passport:
            return 0
    return 1

def main():
    passports = get_input('input.txt')
    valid_passports = 0
    for passport in passports:
        valid_passports += is_valid(passport)
    print(valid_passports)

main()
