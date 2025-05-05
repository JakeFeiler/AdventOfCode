#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    total = 0

    def find_first_and_last(cal_string):
        '''Find the first occurrence of a number and replace it
        Do the same with the last occurrence (unique strings)'''

        list_of_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        locations_of_words = [0] * 9

        #Earliest occurrence of every number string
        for x in range(9):
            locations_of_words[x] = cal_string.find(list_of_words[x])

        #Finding lastest showing of every number string
        backwards_locations_of_words = [0] * 9
        backwards_cal_string = cal_string[::-1]
        for x in range(9):
            backwards_locations_of_words[x] = backwards_cal_string.find(list_of_words[x][::-1])


        #Filter out -1 (numbers don't show up)
        backwards_locations_of_words = list(map(lambda x: x if x >= 0 else 1000, backwards_locations_of_words))
        
        last_digit = backwards_locations_of_words.index(min(backwards_locations_of_words))
        second_string = cal_string.replace(list_of_words[last_digit], str(last_digit + 1))

        #Do the same for the first string, except that there are -1's in the way
        locations_of_words = list(map(lambda x: x if x >= 0 else 1000, locations_of_words))

        first_digit = locations_of_words.index(min(locations_of_words))
        first_string = cal_string.replace(list_of_words[first_digit], str(first_digit + 1))

        return(first_string, second_string)


    for cal_value in s:
        first_replacement, last_replacement = find_first_and_last(cal_value)

        for char in first_replacement:
            if char.isdigit():
                total += 10*int(char)
                break
        for char in last_replacement[::-1]:
            if char.isdigit():
                total += int(char)
                break

    print(total)


main()
