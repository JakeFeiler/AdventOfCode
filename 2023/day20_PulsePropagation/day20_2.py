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



    button_presses = 0
    signal_queue = queue.Queue()

    #rx is a conjunction with conjunction xn input, which has 4 other conjunction inputs
    #Track the periodic high sends to those conjunctions, take a GCD
    required_presses_for_send = {}

    while True:
        button_presses += 1
        for ss in starting_signals:
            signal_queue.put(ss)
        while not signal_queue.empty():
            sending_module, receiving_module, signal_type = signal_queue.get()

            if receiving_module == 'xn' and signal_type == 'h':
                #Found the first (of the periodic) hgh signaals going to xn (goes to rx)
                if sending_module not in required_presses_for_send:
                    required_presses_for_send[sending_module] = button_presses
                #Found them all, here's the answer
                if len(required_presses_for_send) == len(connected_from['xn']):
                    total_button_presses = 1
                    for indiv_required_presses in required_presses_for_send.values():
                        total_button_presses *= indiv_required_presses
                    print(total_button_presses)
                    sys.exit(0)

            is_conjunction = receiving_module in conjunction_modules
            is_ff = receiving_module in ff_modules
            
            if is_ff:
                if signal_type == 'h':
                    continue
                flip_flop_is_on = flip_flop_status_is_on[receiving_module]
                if flip_flop_is_on:
                    next_signal_sent = 'l'
                else:
                    next_signal_sent = 'h'
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
                else:
                    next_signal_sent = 'h'
                for next_connection in connections[receiving_module]:
                    signal_queue.put((receiving_module, next_connection, next_signal_sent))



main()
