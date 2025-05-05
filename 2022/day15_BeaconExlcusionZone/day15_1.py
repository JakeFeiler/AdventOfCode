#!/opt/anaconda3/bin/python
#Jake Feiler

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
    exclusion_zone = set()
    for sensor in s:
        sensor_x, sensor_y, beacon_x, beacon_y = parse_coordinates(sensor)
        sensor_to_beacon = calculate_manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        target_row = 2_000_000
        #Now determine all beacon points on 2000000 that could be in range
        #distance_to_target_row = abs(sensor_y - 2_000_000)
        distance_to_target_row = abs(sensor_y - target_row)        
        ruled_out_horizontal_width = sensor_to_beacon - distance_to_target_row
        if ruled_out_horizontal_width >= 0:
            temp_set = set()
            #Add all points on target row that are within manhatttan distance of the sensor to beacon...
            temp_set.update(list(range(sensor_x - ruled_out_horizontal_width, sensor_x + ruled_out_horizontal_width + 1)))
            #...but don't count a beacon if it's already there
            if beacon_y == target_row:
                temp_set = temp_set.difference(set([beacon_x]))
            exclusion_zone = exclusion_zone.union(temp_set)
    print(len(exclusion_zone))
                     
        

main()
