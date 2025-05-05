#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

class Monkey:
    '''Monkey class'''
    def __init__(self, items, operator, adjustment, divisibility, true_target, false_target):
        '''Set up monkey parameters'''
        self.items = list(items)
        self.operator = operator
        self.adjustment = adjustment
        self.divisibility = divisibility
        self.true_target = true_target
        self.false_target = false_target
        self.total_inspections = 0

    def adjust_worry_level(self, worry_level):
        '''Monkey inspects an item, determine the new worry level'''
        self.total_inspections += 1

        if self.adjustment == 'old':
            adjustment_value = worry_level
        else:
            adjustment_value = int(self.adjustment)
        if self.operator == '+':
            return int((worry_level + adjustment_value)/3)
        else:
            return int(worry_level * adjustment_value/3)

    def find_target(self, value):
        '''Determine who gets this item'''
        if value % self.divisibility == 0:
            return self.true_target
        else:
            return self.false_target

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def clear_items(self):
        self.items = []

    def get_total_checks(self):
        return self.total_inspections
    
def parse_input(input_text):
    
    monkeys = []

    starting_items = []
    operator = ''
    adjustment = 0
    divisibility = 0
    true_target = 0
    false_target = 0
    
    for position, line in enumerate(input_text):
        line_type = position % 7
        if line_type in (0, 6):
            #Monkey 0:
            #
            pass
        elif line_type == 1:
            #Starting items: 63, 84, 80, 83, 84, 53, 88, 72
            starting_items = map(int, (line.split(': ')[1]).split(', '))
        elif line_type == 2:
            #Operation: new = old * 11
            operation = line.split(' ')
            operator, adjustment = operation[-2], operation[-1]
        elif line_type == 3:
            #Test: divisible by 13
            divisibility = int(line.split(' ')[-1])
        elif line_type == 4:
            #If true: throw to monkey 4
            true_target = int(line.split(' ')[-1])
        elif line_type == 5:
            #If false: throw to monkey 7
            false_target = int(line.split(' ')[-1])
            #end of monkey, time to make a new monkey
            monkeys.append(Monkey(starting_items, operator, adjustment, divisibility, true_target, false_target))

    return monkeys
    
        

def main():
    s = get_input('input.txt')
    monkeys = parse_input(s)

    round_number = 1
    while round_number <= 20:
        for monkey in monkeys:
            for item_value in monkey.get_items():
                new_worry_level = monkey.adjust_worry_level(item_value)
                destination = monkey.find_target(new_worry_level)
                monkeys[destination].add_item(new_worry_level)
            monkey.clear_items()
        round_number += 1
        

    monkey_checks = []
    for monkey in monkeys:
        monkey_checks.append(monkey.get_total_checks())
        
    monkey_checks.sort()
    print(monkey_checks[-2] * monkey_checks[-1])

            
main()
