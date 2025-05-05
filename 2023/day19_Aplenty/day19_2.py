#!/opt/anaconda3/bin/python
#Jake Feiler


import sys

def divide_range(x_range, m_range, a_range, s_range, comparison):
    '''Break up the range based on the comparison'''
    aspect = comparison[0]
    comparer = comparison[1]
    value = int(comparison[2:])


    x_range_good = x_range
    m_range_good = m_range
    a_range_good = a_range
    s_range_good = s_range

    x_range_bad = x_range_good
    m_range_bad = m_range_good
    a_range_bad = a_range_good
    s_range_bad = s_range_good

    #Create the ranges that obey/break the rule
    if comparer == '>':
        if aspect == 'x':
            x_range_good = range(max(x_range[0], value + 1), x_range[-1] + 1)
            x_range_bad = range(x_range[0], min(value + 1, x_range[-1] + 1))
        elif aspect == 'm':
            m_range_good = range(max(m_range[0], value + 1), m_range[-1] + 1)
            m_range_bad = range(m_range[0], min(value + 1, m_range[-1] + 1))
        elif aspect == 'a':
            a_range_good = range(max(a_range[0], value + 1), a_range[-1] + 1)
            a_range_bad = range(a_range[0], min(value + 1, a_range[-1] + 1))
        elif aspect == 's':
            s_range_good = range(max(s_range[0], value + 1), s_range[-1] + 1)
            s_range_bad = range(s_range[0], min(value + 1, s_range[-1] + 1))

    elif comparer == '<':
        if aspect == 'x':
            x_range_bad = range(max(x_range[0], value), x_range[-1] + 1)
            x_range_good = range(x_range[0], min(value, x_range[-1] + 1))
        elif aspect == 'm':
            m_range_bad = range(max(m_range[0], value), m_range[-1] + 1)
            m_range_good = range(m_range[0], min(value, m_range[-1] + 1))
        elif aspect == 'a':
            a_range_bad = range(max(a_range[0], value), a_range[-1] + 1)
            a_range_good = range(a_range[0], min(value, a_range[-1] + 1))
        elif aspect == 's':
            s_range_bad = range(max(s_range[0], value), s_range[-1] + 1)
            s_range_good = range(s_range[0], min(value, s_range[-1] + 1))


    return x_range_good, m_range_good, a_range_good, s_range_good, x_range_bad, m_range_bad, a_range_bad, s_range_bad


def find_ranges(x_range, m_range, a_range, s_range, rules, curr_rule):
    '''Determine which ranges  work'''
    valid_ranges = 0

    criteria = rules[curr_rule].split(',')
    for crit in criteria:

        #Check if it's the end
        if crit.find(':') == -1:
            #Rejection - these don't work
            if crit == 'R':
                pass
            #This path works - count these workiing ranges
            elif crit == 'A':
                valid_ranges += len(x_range) * len(m_range) * len(a_range) * len(s_range)
            #This is forced to try another rule
            else:
                next_rule = crit
                valid_ranges += find_ranges(x_range, m_range, a_range, s_range, rules, next_rule)

        else:
            comparison, action = crit.split(':')
            #The good are where the condition is met and wilil follow an action
            #The normal are where the condition isn't met and continues to the next rule
            x_range_good, m_range_good, a_range_good, s_range_good, \
            x_range, m_range, a_range, s_range = divide_range(x_range, m_range, a_range, s_range, comparison)

            #If this is a reject action, ignore these results
            if action == 'R':
                pass
            #If it uses another rule, add this range and recurse
            elif action == 'A':
                valid_ranges += len(x_range_good) * len(m_range_good) * len(a_range_good) * len(s_range_good)
            else:
                next_rule = action
                valid_ranges += find_ranges(x_range_good, m_range_good, a_range_good, s_range_good, rules, next_rule)


    return valid_ranges


def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    rules = {}
    for rule in s:
        if rule == '':
            break
        start_pos = rule.find('{')
        rules[rule[:start_pos]] = rule[start_pos + 1:-1]

    x_range = range(1, 4001)
    m_range = range(1, 4001)
    a_range = range(1, 4001)
    s_range = range(1, 4001)

    valid_ranges = find_ranges(x_range, m_range, a_range, s_range, rules, 'in')
    print(valid_ranges)
main()
