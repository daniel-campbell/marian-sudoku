import sudoku_io

def main():
    board = sudoku_io.load_board("/home/campbell/board.csv")
    sudoku_io.print_board(board)

# grid = [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [0, 1, 2, 3, 4, 5, 9, 9, 9]
#     ]
main()