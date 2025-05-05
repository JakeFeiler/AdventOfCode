#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def hash_algo(step):
    '''Run the algorithm as instructed'''
    value = 0

    for character in step:
        value += ord(character)
        value *= 17
        value %= 256
    return value

def main():
    s = get_input('input.txt')
    sequence = "".join(s).split(',')

    boxes = [ [] for _ in range(256)]


    for step in sequence:
        if step[-1] == '-':
            label = step [:-1]
            box_label = hash_algo(label)
            boxes[box_label] = [lens for lens in boxes[box_label] if lens[0] != label]

        else:
            label = step [:-2]
            box_label = hash_algo(label)

            label_found =  False
            for lens_pos, lens in enumerate(boxes[box_label]):
                if lens[0] == label:
                    boxes[box_label][lens_pos] = tuple([label,step[-1]])
                    label_found = True
                    break
            if not label_found:
                boxes[box_label].append(tuple([label, step[-1]]))

    focusing_power = 0
    for box_num, box in enumerate(boxes):
        for lens_num, lens in enumerate(box):
            focusing_power += (box_num + 1) * (lens_num + 1) * int(lens[1])

    print(focusing_power)

main()
