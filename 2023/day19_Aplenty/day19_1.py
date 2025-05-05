#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

class Part:
    '''aspects of a part'''
    def __init__(self, qualities):
        sections = qualities[1:-1].split(',')
        self.x = int(sections[0][2:])
        self.m = int(sections[1][2:])
        self.a = int(sections[2][2:])
        self.s = int(sections[3][2:])


def validate(part_qualities, rules):
    '''Determine if this part gets accepted, return ratings if so'''
    part = Part(part_qualities)

    current_rule = 'in'
    while True:
        criteria = rules[current_rule].split(',')
        for crit in criteria:

            #Check if it's the end
            if crit.find(':') == -1:
                if crit == 'R':
                    return 0
                elif crit == 'A':
                    return part.x + part.m + part.a + part.s
                else:
                    current_rule = crit
                    break

            else:
                quality = crit[0]
                comparator = crit[1]

                comp_value, result = crit[2:].split(':')
                comp_value = int(comp_value)

                #Use 'getattr' to get the
                old_value = getattr(part, quality)
                #Check if the rule is passed, and follow accordingly
                if (comparator == '<' and old_value < comp_value) or (comparator == '>' and old_value > comp_value):
                    if result == 'R':
                        return 0
                    elif result == 'A':
                        return part.x + part.m + part.a + part.s
                    else:
                        current_rule = result
                        break
                #Otherwise, try the next rule
                else:
                    continue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    rules = {}
    empty_line_pos = 0
    for rule_pos, rule in enumerate(s):
        if rule == '':
            empty_line_pos = rule_pos
            break
        start_pos = rule.find('{')
        rules[rule[:start_pos]] = rule[start_pos + 1:-1]

    final_rating = 0
    for part in s[empty_line_pos + 1:]:
        final_rating  += validate(part, rules)

    print(final_rating)
main()
