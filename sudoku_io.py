import csv

###############################################################################
# print_board
# Prints a 9x9 board to the console
def print_board(board) :
    for i in range(9):
        print(board[i][0], end = " ")
        print(board[i][1], end = " ")
        print(board[i][2], end = " ")
        print("|", end = " ")
        print(board[i][3], end = " ")
        print(board[i][4], end = " ")
        print(board[i][5], end = " ")
        print("|", end = " ")
        print(board[i][6], end = " ")
        print(board[i][7], end = " ")
        print(board[i][8])
        if i == 2 or i == 5:
            print("--------------------")

###############################################################################
# load_board
# loads a board from the given 9x9 CSV file and returns it as a 9x9 array
def load_board(filename) :
    # open the file and initiate the csv reader
    file_handle = open(filename, newline='')
    filereader = csv.reader(file_handle)

    # iterate through the csv row by row and populate the 9x9 gride
    board = [0]*9
    i = 0
    for row in filereader :
        board[i] = row
        i = i + 1

    return board
