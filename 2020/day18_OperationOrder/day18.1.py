#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip()for line in input_file]

def solve_equation(equation):
    '''Given an equation, return the equation's value'''
    standby_val = 1
    standby_op = '*'
    for position, symbol in enumerate(equation):
        #Parenthesis: Recursively solve rest of equation, return when ) is found
        if symbol[0] == '(':
            symbol = solve_equation(equation[position + 1:])
        elif symbol[-1].isdigit():
            if symbol[-1] == ')':
                number = int(symbol[:-1])
            else:
                number = int(symbol)
            if standby_op == '+':
                standby_val += number
            elif standby_op == '*':
                standby_val *= number
        else:
            standby_op = symbol
        if symbol[-1] == ')':
            return standby_val
            

    return standby_val



def main():
    s = get_input('test.txt')

    total_sum = 0
    for equation in s:
        equation = equation.split(' ')
        total_sum += solve_equation(equation)
    print(total_sum)
main()
