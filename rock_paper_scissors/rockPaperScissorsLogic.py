import random

def player_choice(player):
    if player == 'r':
        print("Rock versus...")
    elif player == 'p':
        print("Paper Versus...")
    elif player == 's':
        print("Scissors versus...")

def computer_choice():
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print("ROCK")
    elif random_number == 2:
        computer_move = 'p'
        print("PAPER")
    elif random_number == 3:
        computer_move = 's'
        print("SCISSORS")
    print("")
    return computer_move

def check_win(player, computer):
    if player == computer:
        return 'T'
    elif player == 'r' and computer == 's':
        return 'W'
    elif player == 'p' and computer == 'r':
        return 'W'
    elif player == 's' and  computer == 'p':
        return 'W'
    elif player == 'r' and computer == 'p':
        return 'L'
    elif player == 'p' and computer == 's':
        return 'L'
    elif player == 's' and computer == 'r':
        return 'L'