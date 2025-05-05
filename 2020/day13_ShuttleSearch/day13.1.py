#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    lines = input_file.readlines()
    timestamp = int(lines[0].strip())
    next_line = lines[1].strip().split(',')
    buses = []
    for bus in next_line:
        if bus != 'x':
            buses.append(int(bus))
    return timestamp, buses


def main():
    timestamp, bus_IDS = get_input('input.txt')
    final = 0
    soonest_time = bus_IDS[0]
    for bus_ID in bus_IDS:
        time_to_bus = bus_ID - (timestamp % bus_ID)
        if time_to_bus < soonest_time:
            soonest_time = time_to_bus
            final = time_to_bus * bus_ID
    print(final)


main()
