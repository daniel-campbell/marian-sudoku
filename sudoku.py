from re import I
from sqlite3 import Row
import sudoku_io

###############################################################################
# main
def main():
    # First, load a board
    board = sudoku_io.load_board("board.csv")
    if (board == None) :
        return
    
    sudoku_io.print_board(board)
    
    is_valid_board(board)

    # now, solve the board

###############################################################################
# solve
# will attempt to solve the given board. Will output the results to the console
def solve(board) :
    return

###############################################################################
# is_valid_sudoku_nine
# Returns True if the row is a valid sudoku row. Returns False otherwise. 
def is_valid_sudoku_nine(row) :

    # First, initialize an array of 9 to all False, meaning that we have not
    # found that value yet. Each array entry represents the numbers 1-9
    values = [False, False, False, False, False, False, False, False, False]
    
    # Loop through the inputted row
    for v in row:
        # Look in the "value" array at the index of the number in this iteration
        # of "row". If that value it set to True, it means that we have already 
        # encountered it, so it's a repeat. 
        if values[v-1] == True :
            return False
        
        # 0 means a blank space. If there is a blank space, the line is invalid
        if v == 0 :
            return False
                
        # Otherwise, if we are here, then it's the first time seeing it, so
        # let's just set it to True. 
        values[v-1]=True

        # Print the current list of values to screen, just to debug.
        # print(values)

    # If we got here, it means that we got through the entire row without
    # any repeats, so we know it is a valid row. 
    return True


###############################################################################
# is_valid_board
# Takes a 9x9 sudoku board as input. Returns True iff it is a valid board. 
def is_valid_board(board) :
    
    # FIRST - check all the rows.
    # loop through all rows and return False if we find an invalid row.
    for i in range (9):
        if (is_valid_sudoku_nine(board[i])==False):
            print('Row ' + str(i) + ' is invalid')
            return False
        
    # SECOND - check all the columns.
    # Loop through all the columns and return False if we find an invalid column
    for i in range (9) :
        # Create an array of size 9. 
        column = [0] * 9
        # Fill the column with all the values from board column no. i
        for j in range (9) :
            column[j] = board[j][i]
        #If that column is not valid, return False. 
        if (is_valid_sudoku_nine(column) == False) : 
            print('Column ' + str(i) + ' is invalid')
            return False
        
    # THIRD - check all the 3x3 grids
    # Loop through all the 3x3 grids. 
    for i in range (3) :
        for j in range (3) : 
            # Let's create an 9-int array called "grid" that will contain all the values in this grid that we are looking at. 
            row_iter = i*3
            col_iter = j*3
            grid = [0] * 9
            grid[0] = board[row_iter+0][col_iter+0]
            grid[1] = board[row_iter+0][col_iter+1]
            grid[2] = board[row_iter+0][col_iter+2]
            grid[3] = board[row_iter+1][col_iter+0]
            grid[4] = board[row_iter+1][col_iter+1]
            grid[5] = board[row_iter+1][col_iter+2]
            grid[6] = board[row_iter+2][col_iter+0]
            grid[7] = board[row_iter+2][col_iter+1]
            grid[8] = board[row_iter+2][col_iter+2]
            # If this grid isn't valid, return False.
            if (is_valid_sudoku_nine(grid) == False) :
                print('Grid[' + str(i) + '][' + str(j) + '] is invalid')
                return False
                
    # If we got to this point, then it's a valid board. 
    return True


main()