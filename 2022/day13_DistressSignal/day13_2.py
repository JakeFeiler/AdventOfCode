#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from math import ceil
import functools

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def is_correct_order(left, right, position=0):
    #print(left, right, position)
    '''Are these in the right order, per spec'''
    #Can't use boolean, 3 options
    #-1 -> come before
    #1 -> come after
    #2 -> next element
    
    #First check if position is exceeding length
    #Assume never equal

    #If exhausted a equal list, need to back out
    if position == len(left) and position == len(right):
        return 2
    if position == len(left):
        return -1
    elif position == len(right):
        return 1

    left_value = left[position]
    right_value = right[position]
    left_value_type = type(left_value)
    right_value_type = type(right_value)
    if left_value_type == int and right_value_type == int:
        if left_value == right_value:
            return is_correct_order(left, right, position + 1)
        elif left_value < right_value:
            return -1
        else:
            return 1


    #Not both ints, try converting to lists
    if left_value_type == int:
        left_value = [left_value]
    if right_value_type == int:
        right_value = [right_value]

    inner_list_ordered = is_correct_order(left_value, right_value, 0)
    if inner_list_ordered == 2:
        return is_correct_order(left, right, position + 1)
    else:
        return inner_list_ordered


def turn_into_list(start_point, signal):
    '''Turn this string into a list of ints and lists, starting from start_point'''
    output = []
    #Ignore the first bracket, it means we started this current list
    #signal = signal[1:]
    #outside is the outer brackets

    #If a [ is found, do a recursive run on rest
    #Return/append that recursive list, advance until the ] is found
    while start_point < len(signal):
        bit = signal[start_point]
        if bit == ',':
            pass
        elif bit == ']':
            return output, start_point + 1
        elif bit == '[':
            inner_list, start_point = turn_into_list(start_point + 1, signal)
            output.append(inner_list)
            continue
        else: #(bit is a digit)
            if signal[start_point - 1].isdigit():
                #If consecutive numbers found, adjust final entry into output
                output[len(output) - 1] = 10*output[len(output) - 1] + int(bit)
            else:
                output.append(int(bit))
        start_point += 1
    return output, start_point


def main():
    s = get_input('input.txt')

    divider_1 = [[2]]
    divider_2 = [[6]]

    all_packets = [divider_1, divider_2]
    for x in range(ceil(len(s)/3)):
    #for x in range(1):
        left_input = s[x*3]
        adjusted_left, a = turn_into_list(1, left_input)
        right_input = s[x*3 + 1]
        adjusted_right, b = turn_into_list(1, right_input)
        all_packets.append(adjusted_left)
        all_packets.append(adjusted_right)

    #Using functools' custom key sorter

    all_packets = sorted(all_packets,key=functools.cmp_to_key(is_correct_order))
    index_1 = all_packets.index(divider_1) + 1
    index_2 = all_packets.index(divider_2) + 1
    print(index_1 * index_2)

main()
