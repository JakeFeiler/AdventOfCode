#!/opt/anaconda3/bin/python
#Jake Feiler


#VERY SLOW CODE -> takes 5-10 minutes to run
#Idea - determine candidate locations. Narrows search space down from 16 trillion to
#93 million (and could have been narrowed down more)

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def parse_coordinates(sensor):
    '''Get the coordinates from the line of txt'''
    first_comma = sensor.index(',')
    sensor_x = int(sensor[12:first_comma])
    colon = sensor.index(':')
    sensor_y = int(sensor[first_comma + 4: colon])
    next_comma = sensor.index(',', colon, len(sensor))
    beacon_x = int(sensor[colon + 25: next_comma])
    beacon_y = int(sensor[next_comma + 4:])
    return sensor_x, sensor_y, beacon_x, beacon_y

def calculate_manhattan_distance(x_1, y_1, x_2, y_2):
    return abs(x_1 - x_2) + abs(y_1 - y_2)

def main():
    s = get_input('input.txt')

    #Based on problem spec, all squares with coordinates between 0 and 4,000,000 will be blocked except one
    #Therefore, the beacon should be just 1 square out of range of >= 2 sensors (and only 1 square)
    just_out_of_range_locations = set()
    sensors = set()
    for sensor in s:
        sensor_x, sensor_y, beacon_x, beacon_y = parse_coordinates(sensor)
        sensor_to_beacon = calculate_manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        sensors.add((sensor_x, sensor_y, sensor_to_beacon))
        max_coord = 4_000_000
        x_distance = 0
        y_distance = sensor_to_beacon + 1
        while y_distance >= 0:
            neg_x = sensor_x - x_distance
            pos_x = sensor_x + x_distance
            neg_y = sensor_y - y_distance
            pos_y = sensor_y + y_distance
            if 0 <= pos_y <= max_coord:
                if 0 <= pos_x <= max_coord:
                    just_out_of_range_locations.add((pos_x, pos_y))
                if 0 <= neg_x <= max_coord:
                    just_out_of_range_locations.add((neg_x, pos_y))
            if 0 <= neg_y <= max_coord:
                if 0 <= pos_x <= max_coord:                
                    just_out_of_range_locations.add((pos_x, neg_y))
                if 0 <= neg_x <= max_coord:                    
                    just_out_of_range_locations.add((neg_x, neg_y))
            x_distance += 1
            y_distance -= 1


    #now cycle through these candidate locatiions, determine whats outside everythings range
    for candidate in just_out_of_range_locations:
        candidate_x, candidate_y = candidate[0], candidate[1]
        #Check if we're in the needed range
        #if not (0 <= candidate_x <= max_coord) or not (0 <= candidate_y <= max_coord):
        #    continue
        candidate_is_correct = True
        for sensor in sensors:
            #if candidate_x == 10 and candidate_y == 17:
            #    print(sensor, calculate_manhattan_distance(candidate_x, candidate_y, sensor[0], sensor[1]))
            if calculate_manhattan_distance(candidate_x, candidate_y, sensor[0], sensor[1]) <= sensor[2]:
                candidate_is_correct = False
                break
        if candidate_is_correct:
            print(max_coord * candidate_x + candidate_y)
            break
    del sensors
    del just_out_of_range_locations




main()
