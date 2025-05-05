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

def get_valid_tickets(tickets, allowable_ranges):
    '''Return a list of valid tickets'''
    final_tickets = []
    for nearby_ticket in tickets[1:]:
        stats = nearby_ticket.split(',')
        is_valid = True
        for stat in stats:
            stat = int(stat)
            if stat not in allowable_ranges:
                is_valid = False
                break
        if is_valid:
            final_tickets.append(nearby_ticket)
    return final_tickets

def solve_mappings(final_tickets, possible_mappings, allowable_ranges):
    '''Determine the association from details on tickets to the corresponding column'''
    for ticket in final_tickets:
        ticket_stats = ticket.split(',')
        #Loop through all values on a ticket
        #If a tickets value is not in a detail's possible range
        #Then remove that value from the possibilities for the detail
        for ticket_position, ticket_value in enumerate(ticket_stats):
            ticket_value = int(ticket_value)
            for detail in possible_mappings.keys():
                if ticket_value not in allowable_ranges[detail]:
                    possible_mappings[detail].remove(ticket_position)


    #Solve the mappings sudoku style, use uniqueness to finish problem
    total_possibilities = sum(len(possible_mappings[detail]) for detail in possible_mappings)
    while total_possibilities > len(possible_mappings):
        for detail in possible_mappings:
            if len(possible_mappings[detail]) == 1:
                solved_column = possible_mappings[detail][0]
                for detail_to_be_reduced in possible_mappings:
                    if detail != detail_to_be_reduced and solved_column in possible_mappings[detail_to_be_reduced]:
                        possible_mappings[detail_to_be_reduced].remove(solved_column)
        total_possibilities = sum(len(possible_mappings[detail]) for detail in possible_mappings)

    return possible_mappings


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

    final_tickets = get_valid_tickets(nearby_tickets, allowable_ranges)
    final_tickets.append(my_ticket[1])


    possible_mappings = {}
    for condition in conditions:
        detail = condition.split(":")[0]
        possible_mappings[detail] = list(range(len(conditions)))

    #Set the dictionary mapping ticket details to allowable ranges
    allowable_ranges = {}
    for condition in conditions:
        parts = condition.split(':')
        detail = parts[0]
        parts = parts[1].split(' ')
        range_1, range_2 = parts[1].split('-'), parts[3].split('-')
        start_1, end_1 = int(range_1[0]), int(range_1[1])
        start_2, end_2 = int(range_2[0]), int(range_2[1])
        first_range = list(range(start_1, end_1 + 1))
        second_range = list(range(start_2, end_2 + 1))
        allowable_range = first_range + second_range

        allowable_ranges[detail] = allowable_range

    final_mappings = solve_mappings(final_tickets, possible_mappings, allowable_ranges)

    my_ticket_values = my_ticket[1].split(',')
    final_value = 1
    for detail in final_mappings:
        if detail[:9] == 'departure':
            column = final_mappings[detail][0]
            final_value *= int(my_ticket_values[column])
    print(final_value)





main()
