#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def final_output(board, row, column, last_num_called):
    '''Return the puzzles final output'''
    row = row - row % 5
    column = column - column % 5
    board_sum = 0
    for more_rows in range(5):
        for more_cols in range(5):
            val = board[row + more_rows][column + more_cols]
            if val != 1000:
                board_sum += val
    return board_sum * last_num_called

def main():
    s = get_input('input.txt')
    call_numbers = s[0].split(',')
    call_numbers = list(map(int, call_numbers))
    card_rows = [row.split() for row in s[1:]]
    card_rows = [list(map(int, filter(None, row))) for row in filter(None, card_rows)]

    solved_boards = {}
    for board in range(len(card_rows)//5):
        solved_boards[board] = "F"

    for call_num in call_numbers:
        #go through every card, look for values, update them
        for row_num, card_row in enumerate(card_rows):
            
            #skip if board already solved
            if solved_boards[row_num//5] == "T":
                continue
            
            for col_num, bingo_num in enumerate(card_row):
                if bingo_num == call_num:
                    #set to 1000 - 5000 sum will mean done
                    card_rows[row_num][col_num] = 1000
                if col_num == 4:
                    #Check the row if it's the last column of a card
                    if sum(card_row) == 5000:
                        solved_boards[row_num//5] = "T"
                        #check if all boards are solved
                        if len(set(solved_boards.values())) == 1:
                            print(final_output(card_rows, row_num, col_num, call_num))
                            sys.exit(0)
                if row_num % 5 == 4:
                    #check the column if it's the last row of a card - 5000 sum will mean done
                    col_sum = 0
                    for row_to_sum in range(5):
                        col_sum += card_rows[row_num - row_to_sum][col_num]
                    if col_sum == 5000:
                        solved_boards[row_num//5] = "T"
                        #check if all boards are solved
                        if len(set(solved_boards.values())) == 1:
                            print(final_output(card_rows, row_num, col_num, call_num))
                            sys.exit(0)

main()
