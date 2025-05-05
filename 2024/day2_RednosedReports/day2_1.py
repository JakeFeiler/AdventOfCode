#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def check_if_safe(report):
    report = report.strip().split(' ')
    differences = [int(x) - int(y) for x, y in zip(report[:-1], report[1:])]
    smallest_diff, biggest_diff = min(differences), max(differences)
    if (smallest_diff >= 1 and biggest_diff <= 3) or (smallest_diff >= -3 and biggest_diff <= -1):
        return 1
    return 0

def main():
    s = get_input('input.txt')
    safe_reports = 0
    for report in s:
        safe_reports += check_if_safe(report)
    print(safe_reports)




main()
