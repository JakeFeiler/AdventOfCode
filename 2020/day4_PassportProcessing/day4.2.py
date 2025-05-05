#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import re

def get_input(text):
    '''Read input'''
    input_file = open(text, 'r')
    return input_file.read().split('\n\n')

def is_valid(passport):
    '''Check if passport has all required fields'''
    needed_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for field in needed_fields:
        if field not in passport:
            return 0
    return has_valid_fields(passport)

def has_valid_fields(passport):
    '''Check if every field matches criteria'''
    passport = passport.replace('\n', ' ')
    sections = passport.split(' ')
    for field in sections:
        header, data = field[:3], field[4:]
        if header == 'byr':
            if not 1920 <= int(data) <= 2002:
                return 0
        elif header == 'iyr':
            if not 2010 <= int(data) <= 2020:
                return 0
        elif header == 'eyr':
            if not 2020 <= int(data) <= 2030:
                return 0
        elif header == 'hgt':
            value, metric = int(data[:-2]), data[-2:]
            if metric == 'cm' and not 150 <= value <= 193:
                return 0
            if metric == 'in' and not 59 <= value <= 76:
                return 0
            if metric not in ['cm', 'in']:
                return 0
        elif header == 'hcl':
            lead, color = data[0], data[1:]
            if lead != '#':
                return 0
            for character in color:
                if not character.isdigit() and character not in ['a', 'b', 'c', 'd', 'e', 'f']:
                    return 0
        elif header == 'ecl':
            if data not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return 0
        elif header == 'pid':
            if len(data) != 9 or not data.isdigit():
                return 0
        else:
            continue
    return 1


def main():
    passports = get_input('input.txt')
    valid_passports = 0
    for passport in passports:
        valid_passports += is_valid(passport)
    print(valid_passports)

main()
