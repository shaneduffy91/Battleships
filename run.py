from random import randint
import random


# Creating a 5x5  grid using a nested list to represent the game board.

board = [['.' for _ in range(5)] for _ in range(5)]


# Allow the player to place their ships on the board.

player_ship_row = int(input("Enter the row coordinate for your ship (0-4): "))
player_ship_col = int(input("Enter the column coordinate for your ship (0-4): "))

board[player_ship_row][player_ship_col] = 'S'


# Randomly generate computer's ships.

computer_ship_row = random.randint(0, 4)
computer_ship_col = random.randint(0, 4)

board[computer_ship_row][computer_ship_col] = 'C'


# Gameplay - Guessing the position.

def get_guess():
    row = int(input("Enter your guess for the row (0-4): "))
    col = int(input("Enter your guess for the column (0-4): "))

    # Validation
    while row < 0 or row > 4 or col < 0 or col > 4:
        print("Invalid input. Please enter values between 0 and 4.")
        row = int(input("Enter your guess for the row (0-4): "))
        col = int(input("Enter your guess for the column (0-4): "))

    return row, col

player_turn = True

while True: 
    if player_turn:
        print("Player's Turn")
        guess_row, guess_col = get_guess()

        if guess_row == computer_ship_row and guess_col == computer_ship_col:
            print("Congratulations! You sunk the computer's battleship!")
            board[guess_row][guess_col] = '#'   # Mark the guess with a # for a hit.
            break
        else:
            print("You missed the computer's battleship!")
            board[guess_row][guess_col] = 'X'   # Mark the guess as a miss.
    else:
        print("Computer's turn")
        guess_row = random.randint(0, 4)
        guess_col = random.randint(0, 4)

        if guess_row == player_ship_row and guess_col == player_ship_col:
            print("Oh no! The computer sunk your battleship!")
            board[guess_row][guess_col] = '#'   # Mark the guess with a # for a hit.
            break
        else:
            print("The computer missed your battleship!")
            board[guess_row][guess_col] = 'X'   # Mark the guess as a miss.

    player_turn = not player_turn
    print_board(board)


# Display the game board

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)