#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]

def main():
    jolts = get_input('input.txt')
    jolts.sort()
    initial_jolts = [0]
    jolts = initial_jolts + jolts
    #Able to calculate paths for every value up to maximum voltage
    #Calculate dynamically - add paths reaching previous voltages together
    voltage_paths = [0] * (jolts[-1] + 1)
    voltage_paths[0] = 1
    for position, voltage in enumerate(jolts):
        #Always able to get to current voltage from previous voltage
        voltage_paths[voltage] += voltage_paths[jolts[position - 1]]
        try:
            #If the adapter 2 back is less than 3, add those paths as well
            if voltage - jolts[position - 2] <= 3:
                voltage_paths[voltage] += voltage_paths[jolts[position - 2]]
                #Same for adapter 3 back
                if voltage - jolts[position - 3] == 3:
                    voltage_paths[voltage] += voltage_paths[jolts[position - 3]]
        except:
            continue
        
    total_paths = voltage_paths[-1]
    print(total_paths)

main()
