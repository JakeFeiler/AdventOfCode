#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def is_valid(list_of_differences):
    '''Return if this report is perfect'''
    min_diff = min(list_of_differences)
    max_diff = max(list_of_differences)
    if (-3 <=  min_diff <=  max_diff <= -1) or (1 <= min_diff <= max_diff <= 3):
        return True
    else:
        return False
        

def check_if_safe(report):
    #print(report)
    report = report.strip().split(' ')
    report = list(map(int, report))
    #Reverse the report if it's descending to simplify
    #Making an assumption no fixable report is ascending and first is bigger than last
    if report[0] >= report[-1]:
        report = report[::-1]
    
    differences = [y - x for x, y in zip(report[:-1], report[1:])]
    for diff_pos, diff in enumerate(differences):
        if diff <= 0 or diff >= 4:
            #Bad diff found, try removing both preceding and following value from report
            new_report_1 = report[:diff_pos] + report[diff_pos + 1:]
            new_report_2 = report[:diff_pos + 1] + report[diff_pos + 2:]
            differences_1 = [y - x for x, y in zip(new_report_1[:-1], new_report_1[1:])]
            differences_2 = [y - x for x, y in zip(new_report_2[:-1], new_report_2[1:])]
            return is_valid(differences_1) or is_valid(differences_2)

    #No bad values found, original report was safe
    return True

                                      
def main():
    s = get_input('input.txt')
    safe_reports = 0
    for report in s:
        safe_reports += check_if_safe(report)
    print(safe_reports)




main()
