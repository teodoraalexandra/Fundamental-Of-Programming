from texttable import Texttable

class Board():
    def __init__(self):
        self._data = [[" "]*7 for i in range(6)]

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
        return self._data[r][c] == " "

    @property
    def val(self, i, j):
        return self._data[i][j]

b = Board()
print(b)
