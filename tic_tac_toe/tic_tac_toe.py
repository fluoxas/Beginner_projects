"""
Play the classic game tic tac toe
"""
import game_logic as gl
import sys
import time

print(gl.rules[-1])

player1 = 0
player2 = 0

# main game loop
while True:
    print(f'Player 1 W: {player1}\nPlayer 2 W: {player2}\n')
    
    # check for winner and add points
    winner = gl.check_win()
    if winner == 'p1':
        player1 += 1
        break
    if winner == 'p2':
        player2 += 1
        break

    gl.print_grid()

    # input loop
    while True:
        print(gl.rules[0])
        player_move = input('> ')

        check = gl.check_input(player_move)

        if check:
            if player_move.lower() == 'q':
                sys.exit()
            elif player_move.lower() == '?':
                gl.display_rules()
            else:
                player_move = int(player_move)
        else:
            print('Please enter a valid command.\nFor help use the ? command.\n')
            time.sleep(2)
        
        if type(player_move) == int:
            break

    # display new game board with player marks
    gl.move_placement(player_move)

# need to reset board to loop again without having to break on lines 18-24

if player1 == 1:
    print("Player 1 win")
    sys.exit()
else:
    print("Player 2 win")
    sys.exit()
