#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd
import queue
import numpy as np

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def preliminary_sort(ordered_nodes, connections, first_size):
    '''Return an initial set of x nodes that are connected'''

    nodes_in_group_one = set()
    nodes_to_add = queue.Queue()
    nodes_to_add.put(ordered_nodes[2])

    while len(nodes_in_group_one) < first_size:
        next_node = nodes_to_add.get()
        nodes_in_group_one.add(next_node)
        if next_node in ordered_nodes:
            ordered_nodes.remove(next_node)
        for connected_nodes in connections[next_node]:
            nodes_to_add.put(connected_nodes)

    return list(nodes_in_group_one) + ordered_nodes

def main():
    s = get_input('input.txt')
    connections = dd(list)
    for component in s:
        components = component.split(' ')
        source = components[0][:-1]
        for connected_component in components[1:]:
            connections[source].append(connected_component)
            connections[connected_component].append(source)

    nodes = sorted(connections.keys())

    #Resort to get some initial guess
    group_one_size = 700
    initial_nodes_guess = preliminary_sort(nodes, connections, group_one_size)



    node_count = len(initial_nodes_guess)
    node_order = {node: pos for pos, node in enumerate(initial_nodes_guess)}
    adj_mat = np.zeros((node_count, node_count))
    for node in initial_nodes_guess:
        node_connections = connections[node]
        for neighboring_node in node_connections:
            adj_mat[node_order[node]][node_order[neighboring_node]] = 1

    #Creating a matrix of nxn for all the nodes
    #The two groups are of size x, y (y = n - x)
    #If the sum of the values in the bottom left from rows [x + 1, n) colums [1, x] is 3, the groups are divded
    #Swap rows/columns to get there


    illegal_edges = 0
    while illegal_edges != 3:
        worst_row = 0
        most_wrong = -1*node_count
        #Find the node with the most wrong connections to the other group

        #Avoid 1st and last, so as not to repeat
        for row in range(1,node_count-1):
            net_wrong_connections = most_wrong
            #Allow for some minimum size on the group
            if row < group_one_size and group_one_size > 0.32*node_count:
                #Q1 - right connections in group 1
                #Q2 - wrong connections
                right_connections = np.sum(adj_mat[row, :group_one_size])
                wrong_connections = np.sum(adj_mat[row, group_one_size:])
                net_wrong_connections = wrong_connections - right_connections
            elif row >= group_one_size and group_one_size <= 0.68*node_count:

                #Q3 - wrong connections
                #Q4 - right connections in group 2
                wrong_connections = np.sum(adj_mat[row, :group_one_size])
                right_connections = np.sum(adj_mat[row, group_one_size:])
                net_wrong_connections = wrong_connections - right_connections
            if net_wrong_connections > most_wrong:
                most_wrong = net_wrong_connections
                worst_row = row
        #At the end, move the worst row to the other side
        moving_values = adj_mat[worst_row]
        adj_mat = np.delete(adj_mat, worst_row, 0)
        if worst_row < group_one_size:
            #From group 1 -> group 2
            adj_mat = np.concatenate((adj_mat, [moving_values]))

            #Also move the column
            column = adj_mat[:, worst_row]
            adj_mat = np.delete(adj_mat, worst_row, 1)
            vert_column = column.reshape((-1, 1))
            adj_mat = np.concatenate((adj_mat, vert_column), axis=1)
            group_one_size -= 1
        else:
            #From group 2 -> group 1
            adj_mat = np.concatenate(([moving_values], adj_mat))
            #Also move the column
            column = adj_mat[:, worst_row]
            adj_mat = np.delete(adj_mat, worst_row, 1)
            vert_column = column.reshape((-1, 1))
            adj_mat = np.concatenate((vert_column, adj_mat), axis=1)

            group_one_size += 1
        #Check how many bad connections remain
        illegal_edges = int(np.sum(adj_mat[group_one_size:, :group_one_size]))

    group_two_size = node_count - group_one_size
    print(group_one_size * group_two_size)



main()
