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
    count_x = 0
    count_o = 0
    for i in range(len(board)):
        for j in board[i]:
            if j == X:
                count_x +=1
            if j == O:
                count_o += 1
    if count_x > count_o:
        return O
    else:
        return X
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avaliable = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board [i][j] is None:
                avaliable.add((i,j))
    return avaliable
                
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("invalid action")
    i , j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    elements = [X,O]
    for el in elements:
        for i in range(3):
            if all(board[i][j] == el  for j in range(3) ):
                if el == X:
                    return X
                if el == O:
                    return O

            if all(board[i][i] == el for i in range(3)):
                if el == X:
                    return X
                if el == O:
                    return O

            
            if all(board[i][2 - i] == el for i in range(3)):
                if el == X:
                    return X
                if el == O:
                    return O

            
            if all(board[j][i] == el for j in range(3)):
                if el == X:
                    return X
                if el == O:
                    return O

    return None
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    elements = [X,O]
    for el in elements:
        for i in range(3):                      
            if all(board[i][j] == el  for j in range(3) ):
                return True

            if all(board[i][i] == el for i in range(3)):
                return True
            
            if all(board[i][2 - i] == el for i in range(3)):
                return True
            
            if all(board[j][i] == el for j in range(3)):
                return True
    if all(board [i][j] != None for i in range(3) for j in range(3) ):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
            elements = [X,O]
    for el in elements:
        for i in range(3):
            if all(board[i][j] == el  for j in range(3) ):
                if el == X:
                    return 1
                if el == O:
                    return -1

            if all(board[i][i] == el for i in range(3)):
                if el == X:
                    return 1
                if el == O:
                    return -1

            
            if all(board[i][2 - i] == el for i in range(3)):
                if el == X:
                    return 1
                if el == O:
                    return -1

            
            if all(board[j][i] == el for j in range(3)):
                if el == X:
                    return 1
                if el == O:
                    return -1

    return 0

def max_Value(board):
    v = -math.inf 
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_Value(result(board, action)))
    return v

def min_Value(board):
    v = math.inf 
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_Value(result(board, action)))
    return v

    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        choice = []
        for action in actions(board):
            choice.append([min_Value(result(board,action)),action])
            answer = sorted(choice, key= lambda x: x[0], reverse = True)[0][1]
        return answer
    

    elif player(board) == O:
        choice = []
        for action in actions(board):
            choice.append([max_Value(result(board,action)),action])
            answer = sorted(choice, key= lambda x: x[0], reverse = True)[0][1]        
        return answer
    

    elif terminal(board):
        return None
    