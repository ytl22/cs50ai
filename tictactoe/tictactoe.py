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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    filled = 0
    
    for row in board:
        for move in row:
            if move != EMPTY:
                filled += 1
    if filled == 9:
        return 1

    return O if filled % 2 else X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    

    filled = 0
    unfilled = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                filled += 1
            else:
                unfilled.add((i,j))

    if filled == 9:
        return 1
    else:
        return unfilled
    raise NotImplementedError
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    # Decide the turn
    symbol = player(board)

    # Deep copy the board to a new board
    new_board = copy.deepcopy(board)

    # Add the action to the new board
    new_board[action[0]][action[1]] = symbol

    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # column symbol count
    col_count = {'X': [0,0,0], 'O': [0,0,0]}

    # row check
    for row in board:
        # col check
        for col, symbol in enumerate(row):
            if symbol != EMPTY:
                if col_count[symbol][col] == 2:
                    return symbol
                else: 
                    col_count[symbol][col] += 1

        if EMPTY in row:
            continue
        elif row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # check diagonal
    if board[1][1] != EMPTY:
        # top down diagonal
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        # bottom up diagnoal
        if board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]
    

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check filled
    if actions(board) == 1:
        return True

    # check winner
    if winner(board) != None:
        return True

    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   
    win = winner(board)
    value = {'X':1, 'O':-1}

    try:
        return value[win]
    except: 
        return 0

    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # None for terminal board
    if terminal(board):
        return None

    # X or O turn
    turn = player(board)

    # get available action
    score_action = {-1:[],0:[], 1:[]}
    possible_actions = actions(board)

    lowest = 2
    highest = -2
    for action in possible_actions:
        score = minimax_value(result(board, action))
        score_action[score].append(action)
        lowest = min(lowest, score)
        highest = max(highest, score)

    if turn == X:
        return score_action[highest][0]
    else:
        return score_action[lowest][0]


    raise NotImplementedError

def minimax_value(board):
    '''
    Returns the optimal val for the current player
    '''
    # X or O turn
    turn = player(board)

    possible_actions = actions(board)

    if terminal(board):
        return utility(board)

    if turn == X:
        best_value = -2
        for action in possible_actions:
            value = minimax_value(result(board, action))
            best_value = max(best_value, value)
        return best_value

    elif turn == O:
        best_value = 2
        for action in possible_actions:
            value = minimax_value(result(board, action))
            best_value = min(best_value, value)
        return best_value

