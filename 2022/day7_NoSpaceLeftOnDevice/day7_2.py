#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

class node:
    def __init__(self, name, size, prev_directory):
        '''Node in tree structuree, can be file or directory'''
        self.name = name
        #None size for dirctories
        self.size = size
        self.sub_stuff = []
        self.prev_directory = prev_directory
        self.total_size = None

    def add_sub_thing(self, new_node):
        self.sub_stuff.append(new_node)


    def get_name(self):
        return self.name

    def get_prev_directory(self):
        return self.prev_directory

    def get_sub_stuff(self):
        return self.sub_stuff

    def get_size(self):
        return self.size

    def get_total_size(self):
        '''Get the size of all subfiles and subdirectories
        If it has a small enough size, add to final value'''
        total_size = 0
        for child_node in self.sub_stuff:
            next_size = child_node.get_size()
            if next_size == None:
                total_size += child_node.get_total_size()
            else:
                total_size += int(child_node.get_size())
        #set the total_size for the final part of the task
        self.total_size = total_size
        return total_size

    def get_extra_space(self, needed_space):
        '''Return the best option to have minimal extra space, using this and subdirectories''' 
        if self.size is not None:
            return 30000000
        else:
            #Use it's own total_size if this directory works, otherwise, use a dummy value
            candidate_size = self.total_size
            extra_space = self.total_size - needed_space
            if extra_space < 0:
                candidate_size = 30000000
            next_nodes = self.get_sub_stuff()
            extra_spaces = [next_node.get_extra_space(needed_space) for next_node in next_nodes]
            next_best_option = min(extra_spaces)
            return min (next_best_option, candidate_size)


def main():
    s = get_input('input.txt')

    #hardcode initial node, represented by $ cd /
    ad = node('/', None, None)
    listing = False

    for output in s[1:]:
        if output == '$ ls':
            listing = True
            continue

        if listing == True and output[0] != '$':
            detail, name = output.split(' ')
            if detail == 'dir':
                ad.add_sub_thing(node(name, None, ad))
            else:
                ad.add_sub_thing(node(name, detail, ad))
        else:
            #Must be doing a cd then
            listing = False
            split_command = output.split(' ')
            dir_target = split_command[2]
            if dir_target == '..':
                ad = ad.get_prev_directory()
            else:
                for child in ad.get_sub_stuff():
                    if dir_target == child.get_name():
                        ad = child
                        break

    while ad.get_name() != '/':
        ad = ad.get_prev_directory()
    used_space = ad.get_total_size()
    unused_space = 70000000 - used_space
    needed_space = 30000000 - unused_space

    biggest_dir_size = ad.get_extra_space(needed_space)
    print(biggest_dir_size)
    
 




main()
