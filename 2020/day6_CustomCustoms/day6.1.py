#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r').read().split('\n\n')
    return [line.strip() for line in input_file]

def count_unique_answers(group):
    '''Determine how many questions were answered by anybody from this group'''
    group = "".join(group.split())
    answer_counts = {}
    for answer in group:
        if answer not in answer_counts:
            answer_counts[answer] = 1
    return len(answer_counts)

def main():
    answers = get_input('input.txt')
    total = 0
    for group in answers:
        total += count_unique_answers(group)
    print(total)


main()
