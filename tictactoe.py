"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    if terminal(board):
        return None
    x_count = 0
    o_count = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                x_count += 1
            elif board[row][col] == O:
                o_count += 1
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions_set.add((row, col))

    if len(actions_set) == 0:
        return None
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    board2 = copy.deepcopy(board)
    i, j = action
    board2[i][j] = player(board)
    return board2


def check_row(board, player):
    for row in range(3):
        k = 0
        for column in range(3):
            if board[row][column] == player:
                k += 1
        if k == 3:
            return True
    return False


def check_column(board, player):
    for column in range(3):
        k = 0
        for row in range(3):
            if board[row][column] == player:
                k += 1
        if k == 3:
            return True
    return False


def check_diagonal(board, player):
    if (board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player):
        return True
    if (board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player):
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board, X) or check_column(board, X) or check_diagonal(board, X):
        return X
    if check_row(board, O) or check_column(board, O) or check_diagonal(board, O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (actions(board) == None) or (winner(board) is not None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        moves = []
        for action in actions(board):
            moves.append([min_value(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1]

    if player(board) == O:
        moves = []
        for action in actions(board):
            moves.append([max_value(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0])[0][1]

