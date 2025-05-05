#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_next_secret_num(secret_num):
    '''Calculate the next secret number'''
    mix_produce = secret_num * 64
    secret_num = (secret_num ^ mix_produce) % 16777216

    mix_produce = secret_num//32
    secret_num = (secret_num ^ mix_produce) % 16777216

    mix_produce = secret_num * 2048
    secret_num = (secret_num ^ mix_produce) % 16777216

    return secret_num

def main():
    s = get_input('input.txt')
    total = 0
    for secret_num in s:
        secret_num = int(secret_num)
        for _ in range(2000):
            secret_num = find_next_secret_num(secret_num)
        total += secret_num
    print(total)


main()
