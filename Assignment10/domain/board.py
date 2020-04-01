from texttable import Texttable
import copy

class Square():
    '''
    Represents one square of the game board
    '''

    def __init__(self, row, col):
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

'''
    0 - empty square
    1 - Y
    2 - R 
'''

class Board():
    def __init__(self):
        '''
        Representation of the board
        '''
        self._data = [[0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7]

    def copy(self):
        '''
        Copy the board to make sure we don't alter it while 'thinking ahead'
        '''
        b = Board()
        b._data = copy.deepcopy(self._data)
        return b

    def getEmptySquares(self):
        res = []
        i = 5
        if i == 5:
            for j in range(7):
                if self._data[i][j] == 0:
                    res.append(Square(i, j))
                elif self._data[i-1][j] == 0:
                    res.append(Square(i-1, j))
                elif self._data[i-2][j] == 0:
                    res.append(Square(i-2, j))
                elif self._data[i-3][j] == 0:
                    res.append(Square(i-3, j))
                elif self._data[i-4][j] == 0:
                    res.append(Square(i-4, j))
                elif self._data[i-5][j] == 0:
                    res.append(Square(i-5, j))
        if len(res) == 0:
            i = 4
            if i == 4:
                for j in range(7):
                    if self._data[i][j] == 0:
                        res.append(Square(i, j))
                    elif self._data[i - 1][j] == 0:
                        res.append(Square(i-1, j))
                    elif self._data[i - 2][j] == 0:
                        res.append(Square(i-2, j))
                    elif self._data[i - 3][j] == 0:
                        res.append(Square(i-3, j))
                    elif self._data[i - 4][j] == 0:
                        res.append(Square(i-4, j))
            if len(res) == 0:
                i = 3
                if i == 3:
                    for j in range(7):
                        if self._data[i][j] == 0:
                            res.append(Square(i, j))
                        elif self._data[i - 1][j] == 0:
                            res.append(Square(i-1, j))
                        elif self._data[i - 2][j] == 0:
                            res.append(Square(i-2, j))
                        elif self._data[i - 3][j] == 0:
                            res.append(Square(i-3, j))
                if len(res) == 0:
                    i = 2
                    if i == 2:
                        for j in range(7):
                            if self._data[i][j] == 0:
                                res.append(Square(i, j))
                            elif self._data[i - 1][j] == 0:
                                res.append(Square(i-1, j))
                            elif self._data[i - 2][j] == 0:
                                res.append(Square(i - 2, j))
                    if len(res) == 0:
                        i = 1
                        if i == 1:
                            for j in range(7):
                                if self._data[i][j] == 0:
                                    res.append(Square(i, j))
                                elif self._data[i - 1][j] == 0:
                                    res.append(Square(i-1, j))
                        if len(res) == 0:
                            i = 0
                            if i == 0:
                                for j in range(7):
                                    if self._data[i][j] == 0:
                                        res.append(Square(i, j))

        return res

    def isWon(self):
        d = self._data

        for i in [0, 1, 2, 3, 4, 5]:
            #lines
            if d[i][0] * d[i][1] * d[i][2] * d[i][3] in [1, 16]:
                return True
            if d[i][1] * d[i][2] * d[i][3] * d[i][4] in [1, 16]:
                return True
            if d[i][2] * d[i][3] * d[i][4] * d[i][5] in [1, 16]:
                return True
            if d[i][3] * d[i][4] * d[i][5] * d[i][6] in [1, 16]:
                return True

        for j in [0, 1, 2, 3, 4, 5, 6]:
            #columns
            if d[0][j] * d[1][j] * d[2][j] * d[3][j] in [1, 16]:
                return True
            if d[1][j] * d[2][j] * d[3][j] * d[4][j] in [1, 16]:
                return True
            if d[2][j] * d[3][j] * d[4][j] * d[5][j] in [1, 16]:
                return True

        for j in [0, 1, 2, 3]:
            #diagonals (from left to right)
            if d[5][j] * d[4][j+1] * d[3][j+2] * d[2][j+3] in [1, 16]:
                return True
            if d[4][j] * d[3][j+1] * d[2][j+2] * d[1][j+3] in [1, 16]:
                return True
            if d[3][j] * d[2][j+1] * d[1][j+2] * d[0][j+3] in [1, 16]:
                return True

        for j in [0, 1, 2, 3]:
            #diagonals (from right to left):
            if d[2][j] * d[3][j+1] * d[4][j+2] * d[5][j+3] in [1, 16]:
                return True
            if d[1][j] * d[2][j+1] * d[3][j+2] * d[4][j+3] in [1, 16]:
                return True
            if d[0][j] * d[1][j+1] * d[2][j+2] * d[3][j+3] in [1, 16]:
                return True
        return False

    def isTie(self):
        return self.isWon() == False and len(self.getEmptySquares()) == 0

    '''
    square -  Square instance
    symbol - One of Y(1) or R(2)
    '''

    def move(self, square, symbol):
        ds = {'Y': 1, 'R': 2}

        if square.row not in [0, 1, 2, 3, 4, 5] or square.col not in [0, 1, 2, 3, 4, 5, 6]:
            raise GameException("Move outside board!")
        if symbol not in ['Y', 'R']:
            raise GameException("Invalid symbol!")
        d = self._data

        if d[square.row][square.col] == 0:
            d[square.row][square.col] = ds[symbol]
        elif d[square.row - 1][square.col] == 0:
            d[square.row - 1][square.col] = ds[symbol]
        elif d[square.row - 2][square.col] == 0:
            d[square.row - 2][square.col] = ds[symbol]
        elif d[square.row - 3][square.col] == 0:
            d[square.row - 3][square.col] = ds[symbol]
        elif d[square.row - 4][square.col] == 0:
            d[square.row - 4][square.col] = ds[symbol]
        elif d[square.row - 5][square.col] == 0:
            d[square.row - 5][square.col] = ds[symbol]
        else:
            raise GameException("This column is full!")

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "Y", 2: "R"}

        for i in [0, 1, 2, 3, 4, 5]:
            lst = self._data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()


class GameException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

