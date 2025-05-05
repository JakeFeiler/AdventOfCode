#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def combo(operand, reg_a, reg_b, reg_c):
    '''Perform the combo function'''
    if operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    else:
        return -1

def main():
    s = get_input('input.txt')
    reg_a = int(s[0].split(' ')[-1])
    reg_b = int(s[1].split(' ')[-1])
    reg_c = int(s[2].split(' ')[-1])
    program = list(map(int, s[4].split(' ')[1].split(',')))


    final_result = ''

    inst_pointer = 0
    while True:
        #Try to run the program
        try:
            instruction = program[inst_pointer]
            if instruction == 0:
                operand = combo(program[inst_pointer + 1], reg_a, reg_b, reg_c)
                reg_a = int(reg_a//2**operand)
            elif instruction == 1:
                operand = program[inst_pointer + 1]
                reg_b = reg_b ^ operand
            elif instruction == 2:
                operand = combo(program[inst_pointer + 1], reg_a, reg_b, reg_c)
                reg_b = operand % 8
            elif instruction == 3:
                if reg_a == 0:
                    pass
                else:
                    operand = program[inst_pointer + 1]
                    inst_pointer = operand
            elif instruction == 4:
                reg_b = reg_b ^ reg_c
            elif instruction == 5:
                operand = combo(program[inst_pointer + 1], reg_a, reg_b, reg_c)
                result = operand % 8
                final_result += (str(result) + ',')
            elif instruction == 6:
                operand = combo(program[inst_pointer + 1], reg_a, reg_b, reg_c)
                reg_b = int(reg_a//2**operand)
            elif instruction == 7:
                operand = combo(program[inst_pointer + 1], reg_a, reg_b, reg_c)
                reg_c = int(reg_a//2**operand)

            if instruction == 3 and reg_a != 0:
                pass
            else:
                inst_pointer += 2

            pass
        except:
            break

    print(final_result[:-1])
main()
