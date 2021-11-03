import numpy as np

def display(board):
    """the docstring"""
    n_row, n_col = board.shape
    board_str = ''
    for ii in range(n_row):
        board_str += '\n'
        for jj in range(n_col):
            board_str += ' '
            if board[ii, jj] == 1:
                board_str += 'X'
            elif board[ii, jj] == 2:
                board_str += 'O'
            else:
                board_str += ' '

            if jj != n_col - 1:
                board_str += ' |'

        if ii != n_row - 1:
            board_str += '\n'
            board_str += '---' * (n_col + 1) 
    return board_str

def has_won(board):
    """Check if board wins"""
    # Check rows
    row_check = np.any(board.sum(axis=0) == 3)
    # Check columns
    col_check = np.any(board.sum(axis=1) == 3)
    # Check Diagonals
    first_diag_check = np.trace(board) == 3
    second_diag_check = np.trace(board[::-1]) == 3
    return any([
        row_check,
        col_check,
        first_diag_check,
        second_diag_check,
    ])


if __name__ == '__main__':
    n_row = 3
    n_col = 3
    player1 = np.zeros((n_row, n_col))
    player2 = np.zeros((n_row, n_col))
    display_board = np.zeros((n_row, n_col))

    print('Welcome to tic tac toe')
    print('Enter inputs in the format row col')
    print(display(display_board))
    while True:
        # Player 1 turn
        row, col = input('Enter a row col').split()
        row, col = int(row), int(col)
        player1[row, col] = 1
        display_board[row, col] = 1
        if has_won(player1):
            print('Player 1 wins!')
            break

        print('BOARD AFTER PLAYER 1')
        print(display(display_board))

        # Player 1 turn
        row, col = input('Enter a row col').split()
        row, col = int(row), int(col)
        player2[row, col] = 1
        display_board[row, col] = 2
        if has_won(player2):
            print('Player 2 wins!')
            break

        print('BOARD AFTER PLAYER ')
        print(display(display_board))

