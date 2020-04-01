from texttable import *

class GameException(Exception):
    def __init__(self):
        pass

class Board():
    def __init__(self):
        self._data = [[0] * 3, [0] * 3, [0]*3]

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "X", 2: "0"}

        for i in [0,1,2]:
            lst = self._data[i][:]
            for j in [0,1,2]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()

class Game:
    def __init__(self):
        self._board = Board()

    @property
    def board(self):
        return self._board

    def moveHuman(self, square):
        self._board.move(square, 'X')

    #def moveComputer(self, square):
        #options = self._board.getEmptySquare()
        #self.board.move(choice(options, ' 0')

class UI:
    def __init__(self, g):
        self._game = g

    def _readMove(self):
        while True:
            try:
                tokens = input("Enter move>").split(" ")
                return Square(int(tokens[0]), int(tokens[1]))
            except Exception as e:
                print("Invalid move")

    def start(self):
        b = self._game.board
        print(b)

        move = self._readMove()
        self._game.moveHuman(move)

        self._game.moveComputer(move)

b = Board()
print(b)
g = Game()
print(g)
ui = UI
#ui.start()
