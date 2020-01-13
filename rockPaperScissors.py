# Cli Rock, Paper, Scissors
import sys
import rockPaperScissorsLogic as rps

print('ROCK, PAPER, SCISSORS')

# variables to keep track of score
wins = 0
losses = 0
ties = 0

# main game loop
while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    
    # input loop
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input('> ')

        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print(f"Option '{player_move}' not acceptable.")
        
    # display player choice
    rps.player_choice(player_move)

    # display computer choice
    computer_move = rps.computer_choice()
    
    # check if player won
    result = rps.check_win(player_move, computer_move)

    # record result
    if result == 'W':
        print("You Win!")
        wins += 1
    elif result == 'L':
        print("You Lose!")
        losses += 1
    elif result == 'T':
        print("Tie!")
        ties += 1
    print("")