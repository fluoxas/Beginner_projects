"""
This is the game logic behind tic tac toe
"""

import copy
import random

grid = [
    [' 1 ', '|', ' 2 ', '|', ' 3 '],
    [' - ', '-', ' - ', '-', ' - '],
    [' 4 ', '|', ' 5 ', '|', ' 6 '],
    [' - ', '-', ' - ', '-', ' - '],
    [' 7 ', '|', ' 8 ', '|', ' 9 ']
    ]

possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

template = copy.deepcopy(grid)


# need to add mulitplayer
# need to add ai computer
rules = [
    'Use 1-9 to enter an x in grid',
    'To Reset board enter R',
    # 'For local multiplayer enter M',
    # 'For win conditions enter W',
    'To leave game enter Q',
    'To show list of commands enter ?',

]

valid_commands = ['q', '?']

def print_grid():
    """prints the current board state"""
    for x in range(5):
        for y in range(5):
            print(grid[x][y], end="")
        print()

def reset_board():
    """reset board to play again"""
    pass

def player1_move_placement(location):
    """Prints X on location given"""
    if location == 1:
        grid[0][0] = ' X '
        possible_moves.remove(1)
    elif location == 2:
        grid[0][2] = ' X '
        possible_moves.remove(2)
    elif location == 3:
        grid[0][4] = ' X '
        possible_moves.remove(3)
    elif location == 4:
        grid[2][0] = ' X '
        possible_moves.remove(4)
    elif location == 5:
        grid[2][2] = ' X '
        possible_moves.remove(5)
    elif location == 6:
        grid[2][4] = ' X '
        possible_moves.remove(6)
    elif location == 7:
        grid[4][0] = ' X '
        possible_moves.remove(7)
    elif location == 8:
        grid[4][2] = ' X '
        possible_moves.remove(8)
    elif location == 9:
        grid[4][4] = ' X '
        possible_moves.remove(9)

def player2_move_placement(location):
    """Prints X on location given"""
    if location == 1:
        grid[0][0] = ' O '
        possible_moves.remove(1)
    elif location == 2:
        grid[0][2] = ' O '
        possible_moves.remove(2)
    elif location == 3:
        grid[0][4] = ' O '
        possible_moves.remove(3)
    elif location == 4:
        grid[2][0] = ' O '
        possible_moves.remove(4)
    elif location == 5:
        grid[2][2] = ' O '
        possible_moves.remove(5)
    elif location == 6:
        grid[2][4] = ' O '
        possible_moves.remove(6)
    elif location == 7:
        grid[4][0] = ' O '
        possible_moves.remove(7)
    elif location == 8:
        grid[4][2] = ' O '
        possible_moves.remove(8)
    elif location == 9:
        grid[4][4] = ' O '
        possible_moves.remove(9)

def display_rules():
    """display rules"""
    for i, rule in enumerate(rules):
        print(f'{i}. {rule}')

def check_win():
    """check to see if player has won and add score to winner"""
    result_col = check_columns()
    result_diag = check_diag()
    result_row = check_rows()

    if result_col:
        if result_col == 'X':
            return 'p1'
        else:
            return 'p2'
    
    if result_diag:
        if result_diag == 'X':
            return 'p1'
        else:
            return 'p2'
    
    if result_row:
        if result_row == 'X':
            return 'p1'
        else:
            return 'p2'

def check_rows():
    """check all rows on board for winner"""
    if grid[0][0] == ' X ' and grid[0][2] == ' X ' and grid[0][4] == ' X ':
        return 'X'
    elif grid[0][0] == ' O ' and grid[0][2] == ' O ' and grid[0][4] == ' O ':
        return 'O'
    elif grid[2][0] == ' X ' and grid[2][2] == ' X ' and grid[2][4] == ' X ':
        return 'X'
    elif grid[2][0] == ' O ' and grid[2][2] == ' O ' and grid[2][4] == ' O ':
        return 'O'
    elif grid[4][0] == ' X ' and grid[4][2] == ' X ' and grid[4][4] == ' X ':
        return 'X'
    elif grid[4][0] == ' O ' and grid[4][2] == ' O ' and grid[4][4] == ' O ':
        return 'O'
    else:
        return False

def check_columns():
    """check all columns for winner"""
    if grid[0][0] == ' X ' and grid[2][0] == ' X ' and grid[4][0] == ' X ':
        return 'X'
    elif grid[0][0] == ' O ' and grid[2][0] == ' O ' and grid[4][0] == ' O ':
        return 'O'
    elif grid[0][2] == ' X ' and grid[2][2] == ' X ' and grid[4][2] == ' X ':
        return 'X'
    elif grid[0][2] == ' O ' and grid[2][2] == ' O ' and grid[4][2] == ' O ':
        return 'O'
    elif grid[0][4] == ' X ' and grid[2][4] == ' X ' and grid[4][4] == ' X ':
        return 'X'
    elif grid[0][4] == ' O ' and grid[2][4] == ' O ' and grid[4][4] == ' O ':
        return 'O'
    else:
        return False

def check_diag():
    """check all diagnols for winner"""
    if grid[0][0] == ' X ' and grid[2][2] == ' X ' and grid[4][4] == ' X ':
        return 'X'
    elif grid[0][0] == ' O ' and grid[2][2] == ' O ' and grid[4][4] == ' O ':
        return 'O'
    elif grid[0][4] == ' X ' and grid[2][2] == ' X ' and grid[4][0] == ' X ':
        return 'X'
    elif grid[0][4] == ' O ' and grid[2][2] == ' O ' and grid[4][0] == ' O ':
        return 'O'
    else:
        return False

def computer_move():
    """defines the computers move currently randomly selected
    latter version will include ai?"""
    computer = random.choice(possible_moves)
    player2_move_placement(computer)

def check_input(command):
    """check user input for command or valid int (1-9)"""
    if command == "":
        return False
    elif command in valid_commands:
        return True
    else:
        try:
            command = int(command)
            if command > 0 and command < 10:
                return True
        except ValueError:
            return False
        except TypeError:
            return False
        