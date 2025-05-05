#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict
from collections import Counter

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r').read().split('\n\n')
    return [line.strip() for line in input_file]

def count_unique_answers(group):
    '''Determine how many questions were answered by anybody from this group'''
    people_count = group.count('\n') + 1
    group = "".join(group.split())
    answer_counts = defaultdict(int)
    for answer in group:
        answer_counts[answer] += 1
    answer_frequencies = Counter(answer_counts.values())
    return answer_frequencies[people_count]

def main():
    answers = get_input('input.txt')
    total = 0
    for group in answers:
        total += count_unique_answers(group)
    print(total)


main()
