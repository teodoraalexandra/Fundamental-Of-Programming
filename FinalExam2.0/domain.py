from texttable import Texttable
from random import choice


class Board():
    def __init__(self):
        self._data = [[' ']*8 for i in range(8)]

    def __str__(self):
        t = Texttable()
        for line in range(8):
                t.add_row(self._data[line])

        t.header(["0", "1", "2", "3", "4", "5", "6", "7"])
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

    def placeStars(self):
        squares = []
        for i in range(8):
            for j in range(8):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        possible = []
        for i in squares:
            if self.checkAdiacent(i):
                possible.append([i[0], i[1]])

        for i in range(10):
            poss = choice(possible)
            self.board.move(poss[0], poss[1], "*")


    def placeUSS(self):
        squares = []
        for i in range(8):
            for j in range(8):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        square = choice(squares)
        r = square[0]
        c = square[1]
        self.board.move(r, c, "E")

    def placeBlingon(self):
        squares = []
        for i in range(8):
            for j in range(8):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        square = choice(squares)
        r = square[0]
        c = square[1]
        self.board.move(r, c, "B")

        squares = []
        for i in range(8):
            for j in range(8):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        square = choice(squares)
        r = square[0]
        c = square[1]
        self.board.move(r, c, "B")

        squares = []
        for i in range(8):
            for j in range(8):
                if self.board.getEmptySquare(i, j):
                    squares.append([i, j])

        square = choice(squares)
        r = square[0]
        c = square[1]
        self.board.move(r, c, "B")

    def checkAdiacent(self, i):
        r = i[0]
        c = i[1]

        if r == 0:
            if c == 0:
                if self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r+1, c+1):
                    return True
            elif c == 7:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c-1):
                    return True
            else:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r+1, c-1) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r+1, c+1):
                    return True
        elif r == 7:
            if c == 0:
                if self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c+1):
                    return True
            elif c == 7:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c-1):
                    return True
            else:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r-1, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c+1):
                    return True
        elif c == 0:
            if r == 0:
                if self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r+1, c+1):
                    return True
            elif r == 7:
                if self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c+1):
                    return True
            else:
                if self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r-1, c+1) and self.board.getEmptySquare(r, c+1) and self.board.getEmptySquare(r+1, c+1):
                    return True
        elif c == 7:
            if r == 0:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c-1):
                    return True
            elif r == 7:
                if self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1, c-1):
                    return True
            else:
                if self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r-1, c-1) and self.board.getEmptySquare(r, c-1) and self.board.getEmptySquare(r+1, c-1):
                    return True
        else:
            if self.board.getEmptySquare(r-1, c-1) and self.board.getEmptySquare(r-1, c) and self.board.getEmptySquare(r-1,c +1) and self.board.getEmptySquare(r, c - 1) and self.board.getEmptySquare(r, c + 1) and self.board.getEmptySquare(r+1, c - 1) and self.board.getEmptySquare(r+1, c) and self.board.getEmptySquare(r+1, c + 1):
                return True

