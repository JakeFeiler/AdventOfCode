#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    s = [line.strip() for line in input_file]
    c, m, n = [], [], []
    section = 1
    for line in s:
        if line == '':
            section += 1
            continue
        if section == 1:
            c.append(line)
        elif section == 2:
            m.append(line)
        else: #section == 3
            n.append(line)
    return c, m, n


def main():
    conditions, my_ticket, nearby_tickets = get_input('input.txt')
    allowable_ranges = set()
    for condition in conditions:
        parts = condition.split(':')
        parts = parts[1].split(' ')
        range_1, range_2 = parts[1].split('-'), parts[3].split('-')
        start_1, end_1 = int(range_1[0]), int(range_1[1])
        start_2, end_2 = int(range_2[0]), int(range_2[1])
        first_range = list(range(start_1, end_1 + 1))
        second_range = list(range(start_2, end_2 + 1))
        allowable_ranges.update(first_range)
        allowable_ranges.update(second_range)

    scanning_error_rate = 0
    for nearby_ticket in nearby_tickets[1:]:
        stats = nearby_ticket.split(',')
        for stat in stats:
            stat = int(stat)
            if stat not in allowable_ranges:
                scanning_error_rate += int(stat)

    print(scanning_error_rate)


main()
