import sudoku_io

###############################################################################
# main
def main():
    board = sudoku_io.load_board("/home/campbell/board.csv")
    sudoku_io.print_board(board)
    is_valid_board(board)


###############################################################################
# is_valid_row
# Returns True if the row is a valid sudoku row. Returns False otherwise. 
def is_valid_row(row) :

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
        
        # Otherwise, if we are here, then it's the first time seeing it, so
        # let's just set it to True. 
        values[v-1]=True

        # Print the current list of values to screen, just to debug.
        print(values)

    # If we got here, it means that we got through the entire row without
    # any repeats, so we know it is a valid row. 
    return True 


###############################################################################
# is_valid_board
# Takes a 9x9 sudoku board as input. Returns True iff it is a valid board. 
def is_valid_board(board) :
    
    # loop through all rows and return False if we find an invalid row.
    for i in range (9):
        if (is_valid_row(board[i])==False):
            return False
        
    # Loop through all the COLUMNS and return False if we find an invalid column
    # TODO <-- Start here

    # Loop through all the 3x3 boxes and return False if we find an invalid 3x3
    # TODO <-- do this next

    # If we got to this point, then it's a valid board. 
    return True


main()