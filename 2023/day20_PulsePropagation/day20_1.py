#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import queue
from collections import defaultdict
import time

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    #Which are the conjunctoins
    conjunction_modules = []
    #which are the flipflops
    ff_modules = []
    #What every module connects to
    connections = defaultdict(list)
    #Connections leading to conjunctions
    connected_from = defaultdict(lambda: defaultdict(str))

    flip_flop_status_is_on = {}
    #False = off, True = on
    starting_signals = []

    for module in s:
        module = module.split(' -> ')
        sending_module = module[0][1:]
        connected_modules = module[1].split(', ')
        if module[0] == 'broadcaster':
            for first_dest in connected_modules:
                starting_signals.append(('broadcaster', first_dest, 'l'))
            continue
        elif module[0][0] == '&':
            conjunction_modules.append(sending_module)
        elif module[0][0] == '%':
            ff_modules.append(sending_module)
            flip_flop_status_is_on.update({sending_module: False})
        connections[sending_module] = connected_modules

        #Will have redundant entries for flip-flops
        for next_module in connected_modules:
            connected_from[next_module][sending_module] = 'l'



    button_press_count = 1000
    signal_queue = queue.Queue()
    hp_count = 0
    lp_count = button_press_count*(len(starting_signals) + 1)

    for button_press in range(button_press_count):
        for ss in starting_signals:
            signal_queue.put(ss)
        while not signal_queue.empty():
            sending_module, receiving_module, signal_type = signal_queue.get()

            is_conjunction = receiving_module in conjunction_modules
            is_ff = receiving_module in ff_modules
            
            if is_ff:
                if signal_type == 'h':
                    continue
                flip_flop_is_on = flip_flop_status_is_on[receiving_module]
                if flip_flop_is_on:
                    next_signal_sent = 'l'
                    lp_count += len(connections[receiving_module])
                else:
                    next_signal_sent = 'h'
                    hp_count += len(connections[receiving_module])
                flip_flop_status_is_on[receiving_module] = not flip_flop_is_on
                for next_connection in connections[receiving_module]:
                    signal_queue.put((receiving_module, next_connection, next_signal_sent))
            elif is_conjunction:
                connected_from[receiving_module][sending_module] = signal_type
                all_high = True
                for state in connected_from[receiving_module].values():
                    if state == 'l':
                        all_high = False
                if all_high:
                    next_signal_sent = 'l'
                    lp_count += len(connections[receiving_module])
                else:
                    next_signal_sent = 'h'
                    hp_count += len(connections[receiving_module])
                for next_connection in connections[receiving_module]:
                    signal_queue.put((receiving_module, next_connection, next_signal_sent))

    print(lp_count * hp_count)


main()
