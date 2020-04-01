from texttable import Texttable
from random import choice


class Board():
    def __init__(self):
        self._data = [[' ']*6 for i in range(6)]

    def __str__(self):
        t = Texttable()
        for line in range(6):
                t.add_row(self._data[line])

        return t.draw()

    def move(self, r, c, s):
        self._data[r][c] = s

    def getValue(self, r, c):
        return self._data[r][c]

    def getEmptySquare(self, r, c):
        return self._data[r][c] == ' '

    @property
    def val(self, i, j):
        return self._data[i][j]


class Game():
    def __init__(self):
        self.board = Board()

    def moveHuman(self, r, c):
        s = 'X'
        self.board.move(r, c, s)
        self.stars(r, c)

    def stars(self, r, c):
        if r == 0:
            if c == 0:
                self.board.move(r, c + 1, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r + 1, c + 1, '*')
            elif c == 5:
                self.board.move(r, c - 1, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r + 1, c - 1, '*')
            else:
                self.board.move(r, c + 1, '*')
                self.board.move(r, c - 1, '*')
                self.board.move(r + 1, c - 1, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r + 1, c + 1, '*')
        elif r == 5:
            if c == 0:
                self.board.move(r - 1, c, '*')
                self.board.move(r - 1, c + 1, '*')
                self.board.move(r, c + 1, '*')
            elif c == 5:
                self.board.move(r - 1, c, '*')
                self.board.move(r - 1, c - 1, '*')
                self.board.move(r, c - 1, '*')
            else:
                self.board.move(r - 1, c - 1, '*')
                self.board.move(r - 1, c, '*')
                self.board.move(r - 1, c + 1, '*')
                self.board.move(r, c - 1, '*')
                self.board.move(r, c + 1, '*')
        elif c == 0:
            if r == 0:
                self.board.move(r, c + 1, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r + 1, c + 1, '*')
            elif r == 5:
                self.board.move(r - 1, c, '*')
                self.board.move(r - 1, c + 1, '*')
                self.board.move(r, c + 1, '*')
            else:
                self.board.move(r - 1, c, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r - 1, c + 1, '*')
                self.board.move(r, c + 1, '*')
                self.board.move(r + 1, c + 1, '*')
        elif c == 5:
            if r == 0:
                self.board.move(r, c - 1, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r + 1, c - 1, '*')
            elif r == 5:
                self.board.move(r - 1, c, '*')
                self.board.move(r - 1, c - 1, '*')
                self.board.move(r, c - 1, '*')
            else:
                self.board.move(r - 1, c, '*')
                self.board.move(r + 1, c, '*')
                self.board.move(r - 1, c - 1, '*')
                self.board.move(r, c - 1, '*')
                self.board.move(r + 1, c - 1, '*')
        else:
            self.board.move(r-1, c-1, '*')
            self.board.move(r-1, c, '*')
            self.board.move(r-1, c+1, '*')

            self.board.move(r+1, c-1, '*')
            self.board.move(r+1, c, '*')
            self.board.move(r+1, c+1, '*')

            self.board.move(r, c-1, '*')
            self.board.move(r, c+1, '*')

    def moveComputer(self):
        s = 'O'
        squares = []
        for i in range(6):
            for j in range(6):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        square = choice(squares)
        r = square[0]
        c = square[1]
        self.board.move(r, c, s)
        self.stars(r, c)

    def isWon(self):
        square = 0
        for i in range(6):
            for j in range(6):
                if self.board.getEmptySquare(i, j):
                    square += 1
        if square > 0:
            return False
        return True
