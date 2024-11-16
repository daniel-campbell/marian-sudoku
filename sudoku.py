import sudoku_io
import time
import os

###############################################################################
# main
def main():
    directory = "boards"    

    boards = []
    times = []

    for filename in os.listdir(directory) :
        if filename.lower().endswith('.csv') : 
            file_path = os.path.join(directory, filename)
            execution_time = solve_csv(file_path)
            boards.append(filename)
            times.append(execution_time)
            
    for i in range(len(boards)) :
        print(f"{boards[i]}\t{times[i]}")
            
    
###############################################################################
# solve_csv
def solve_csv(filename) :
    # Capture the starting time
    print(f"Capturing starting time now for board '{filename}'")
    start_time = time.time()

    # First, load a board
    board = sudoku_io.load_board(filename)
    if (board == None) :
        return -1
    
    # print  the board that we just loaded
    print("Starting board is: ")  
    sudoku_io.print_board(board)
    print("Solving...")

    # now, solve the board
    if solve(board) :
        print("Solution: ")
        sudoku_io.print_board(board)
    else : 
        print("No solution!")

    # Now capture the end time of the execution
    end_time = time.time()
    execution_time = end_time - start_time
    print("End time captured.")
    print(f"Execution time was {execution_time:.6f} seconds")
    print("Thanks for playing!")
    print("-------------------------------------------------------------------------------")
    return execution_time
    

###############################################################################
# solve
# will attempt to solve the given board. Will output the results to the console
def solve(board) :
    # Find the first empty cell we can find. 
    row_and_col = find_empty(board) 
    if not row_and_col : 
        return True
    else:
        row, col = row_and_col
        
    # Iterate through all the possible sudoku numbers to see if it is valid in this spot of the board. 
    for num in range(1, 10) :
        # print('Trying row, col, num: ', row, col, num)
        board[row][col]=num
        if is_valid_board (board) :
            if solve(board) :
                return True
        board[row][col] = 0
            
    
    #Otherwise, we return false        
    return False


###############################################################################
# is_valid_sudoku_nine
# Returns True if the row is a valid sudoku row. Returns False otherwise. 
def is_valid_sudoku_nine(row) :

    # First, initialize an array of 9 to all False, meaning that we have not
    # found that value yet. Each array entry represents the numbers 1-9
    values = [False, False, False, False, False, False, False, False, False]
    
    # Loop through the inputted row
    for v in row:
        # if this is a '0' cell, then we will just skip over it and consider it valid
        if v != 0 :
            # Look in the "value" array at the index of the number in this iteration
            # of "row". If that value it set to True, it means that we have already 
            # encountered it, so it's a repeat. 
            if values[v-1] == True :
                return False
                
            # Otherwise, if we are here, then it's the first time seeing it, so
            # let's just set it to True. 
            values[v-1]=True

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
            # print('Row ' + str(i) + ' is invalid')
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
            # print('Column ' + str(i) + ' is invalid')
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
                # print('Grid[' + str(i) + '][' + str(j) + '] is invalid')
                return False
                
    # If we got to this point, then it's a valid board. 
    return True


################################################################################################################################
# find_empty will find an empty cell and return the column and row number
def find_empty(board):
    for i in range (9) :
        for j in range (9) :
            if board [i][j]==0 :
                return (i,j)
    return None


main()