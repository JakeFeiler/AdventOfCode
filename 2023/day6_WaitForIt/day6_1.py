#!/opt/anaconda3/bin/python
#Jake Feiler


import sys
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    #Starting time = T
    #Distance = d
    #hold time/speed = t
    #t*(T-t) >= D
    #-t^2 +Tt - D >= 0
    #t^2 - Tt + D = 0
    #t = (T +- sqrt(T^2 - 4D))/2

    times = s[0].split(' ')[1:]
    distances = s[1].split(' ')[1:]
    times = list(filter(None, times))
    distances = list(filter(None, distances))

    total_ways = 1

    for race in range(len(times)):
        time, distance = int(times[race]), int(distances[race])
        slowest_hold = math.ceil((time -  math.sqrt(time**2 - 4*distance))/2)
        longest_hold = math.floor((time +  math.sqrt(time**2 - 4*distance))/2)

        #Dont allow for ties
        if slowest_hold * (time - slowest_hold) == distance:
            slowest_hold += 1
        if longest_hold * (time - longest_hold) == distance:
            longest_hold -= 1

        total_ways *= (longest_hold - slowest_hold + 1)

    print(total_ways)





main()
