from  random import randint


scores = {"computer": 0, "player": 0 }

class Battleship_board():
    """
    Main Battleship board class. This sets the size of the board, 
    the number of ships, the player's name and the type of board 
    (ie. player board or computer). It has a method for adding the
    grid and ships, in addition to printing the battleship board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

#player_board = Battleship_board("8", "5", "Shane", "game")
#print(player_board)
#print(player_board.size)
#print(player_board.num_ships)
#print(player_board.name)


def print(self):
    for row in self.board:
        print(" ".join(row))

def guesses(self, x, y):
    self.guesses.append((x, y))
    self.board[x] [y] = "x"

def random_point(size):
    """
    Helper function to return a random
    integer between 0 and size of board.
    """

    return randint(0, size -1)


def validate_coordinates(x, y, board):
    pass

def create_ships(board):
    Computer_board = [[''] * 8 for x in range(8)]
    Player_board = [[''] * 8 for x in range(8)]


def make_guess(board):
    pass

def play_game(computer_board, player_board):
    pass






def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initializes the board.
    """

    size = 8
    num_ships = 5
    scores ["computer"] = 0   
    scores ["player"] = 0  
    print("-" * 35)
    print("Welcome to Mega Battleships")
    print(f" Board Size: {size}, Number of Ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Battleship_board(size, num_ships, "Computer", type="computer")
    player_board  = Battleship_board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

        play_game(computer_board, player_board)


new_game()        