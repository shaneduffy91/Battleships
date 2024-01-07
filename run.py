from  random import randint


scores = {"computer": 0, "player": 0 }

class Battleship_board
"""
Main Battleship board class. This sets the size of the board, 
the number of ships, the player's name and the type of board 
(ie. player board or computer). It has a method for adding the
grid and ships, in addition to printing the battleship board.
"""

def _init_self(self, size, num_ships, name, type):
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

def guesses(self, x, y):
    self.guesses.append((x, y))
    self.board[x] [y] = "x"
