from random import randint
import random

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets the board size, the number of ships,
    the player's name and the board type (player board or computer).
    Has methods for adding ships, adding guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "#"
            return "You sunk the battleship!"
            scores += 1
        else:
            return "You missed the battleship!"

    def add_ships(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "S"

    def random_point(size):
        """
        Helper function to return a random integer between 0 and size.
        """
        return randint(0, size - 1)


def validate_coordinates(x, y, board):
    if x < 0 or x >= board.size:
        print("Invalid coordinate, please enter a valid row number!")
        return False
    elif y < 0 or y >= board.size:
        print("Invalid coordinate, please enter a valid column number!")
        return False
    elif not isinstance(x, int) or not isinstance(y, int):
        print("Invalid coordinate, please enter a valid number!")
        return False
    elif (x, y) in board.guesses:
        print("Coordinate has already been guessed, please try again!")
        return False


def populate_board(board):
    x = (random.randint(0, board.size - 1))
    y = (random.randint(0, board.size - 1))
    board.add_ships(x, y)
    print(board)


def make_guess(board):
    row = int(input("Enter your guess for the row (0-5): "))
    col = int(input("Enter your guess for the column (0-5): "))
    if validate_coordinates(row, col, board):
        result = board.guess(row, col)
        print(result)


def play_game(computer_board, player_board):
    print(player_board)
    print(computer_board)

    while True:
        print("Your Turn")
        make_guess(player_board)
        print("Computer's turn")
        populate_board(computer_board)


def new_game():
    """
    Starts a new game. Sets a board size and number of ships, resets the scores
    and initializes the board.
    """

    size = 6
    num_ships = 5
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome To Mega Battleships")
    print(f"Board Size: {size}. Number of Ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please Enter Your Name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "computer", type ="computer")
    player_board = Board(size, num_ships, player_name, type ="player")

    for _ in range (num_ships):
        populate_board(player_board)
        populate_board(computer_board)

        play_game(computer_board, player_board)


new_game()
