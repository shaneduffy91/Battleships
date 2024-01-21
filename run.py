from random import randint
import random

# Create grid for the player
grid_size = 6  # Adjust the grid size as per your preference
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Create grid for the computer
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

def place_ships(grid, num_ships):
    for _ in range(num_ships):
        ship_placed = False
        while not ship_placed:
            ship_row = random.randint(0, grid_size - 1)
            ship_col = random.randint(0, grid_size - 1)
            if grid[ship_row][ship_col] == '.':
                grid[ship_row][ship_col] = 'S'
                ship_placed = True

def validate_guess(guess):
    try:
        guess = int(guess)
    except ValueError:
        return False

    if guess < 0 or guess >= grid_size:
        return False

    return True


def play_game():
    game_over = False

    while not game_over:
        # Print the player's grid
        print("Player grid:")
        for row in player_grid:
            print(' '.join(row))
        print()

        # Ask the player for a guess
        guess_row = int(input("Enter row guess: "))
        guess_col = int(input("Enter column guess: "))

        # Validate the player's guess
        if not validate_guess(guess_row) or not validate_guess(guess_col):
            print("Invalid guess! Please try again.")
            continue

        # Check if the player has already guessed the same position
        if player_grid[guess_row][guess_col] != '.':
            print("You have already guessed this position! Please try again.")
            continue

        # Check if player enters a string insted of a number
        if player_grid[guess_row][guess_col] == " ":
            print("You must enter a number! Try again.")

        # Check if the player's guess is a hit or a miss
        if computer_grid[guess_row][guess_col] == 'S':
            print("You got a hit!")
            computer_grid[guess_row][guess_col] = 'X'
        else:
            print("You missed!")

        # Check if the game is over
        player_wins = all(all(cell != 'S' for cell in row) for row in computer_grid)
        computer_wins = all(all(cell != 'S' for cell in row) for row in player_grid)

        if player_wins or computer_wins:
            break

        # Computer's turn
        print("Computer's turn...")

        # Generate random guess for the computer
        computer_guess_row = random.randint(0, grid_size - 1)
        computer_guess_col = random.randint(0, grid_size - 1)

        # Validate the computer's guess
        while player_grid[computer_guess_row][computer_guess_col] != 'O':
            computer_guess_row = random.randint(0, grid_size - 1)
            computer_guess_col = random.randint(0, grid_size - 1)

        # Check if the computer's guess is a hit or a miss
        if player_grid[computer_guess_row][computer_guess_col] == 'S':
            print("Computer got a hit!")
            player_grid[computer_guess_row][computer_guess_col] = 'X'
        else:
            print("Computer missed!")

        # Check if the game is over
        player_wins = all(all(cell != 'S' for cell in row) for row in computer_grid)
        computer_wins = all(all(cell != 'S' for cell in row) for row in player_grid)

        if player_wins or computer_wins:
            break

    # Print the final grid of the winner
    if player_wins:
        print("Player wins!")
        print("Final player grid:")
        for row in player_grid:
            print(' '.join(row))
    else:
        print("Computer wins!")
        print("Final computer grid:")
        for row in computer_grid:
            print(' '.join(row))


# Player places ships
place_ships(player_grid, 5)

# Computer places ships
place_ships(computer_grid, 5)

# Start the game
play_game()
