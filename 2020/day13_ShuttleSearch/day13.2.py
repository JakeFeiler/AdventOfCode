#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    lines = input_file.readlines()
    line = lines[1].strip().split(',')
    buses = []
    for position, bus in enumerate(line):
        if bus != 'x':
            buses.append([position, int(bus)])
    return buses


def main():
    buses = get_input('input.txt')

    #Chinese Remainder Theorem
    #First is 0 mod ID
    #Second is -1 mod ID
    #Fourth is -3 mod ID, etc

    for bus_id in buses:
        bus_id[0] = (bus_id[1] - bus_id[0]) % bus_id[1]

    #Solve by sieving
    buses.sort(key=lambda x: x[1], reverse=True)
    minute = buses[0][0]
    increment = buses[0][1]
    current_bus_to_check = 1
    while current_bus_to_check < len(buses):
        minute += increment
        if minute % buses[current_bus_to_check][1] == buses[current_bus_to_check][0]:
            increment *= buses[current_bus_to_check][1]
            current_bus_to_check += 1
    print(minute)


main()
