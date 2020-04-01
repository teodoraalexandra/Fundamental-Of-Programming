from texttable import Texttable

class Square():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def row(self):
        return self.__x

    @property
    def col(self):
        return self.__y


class Board:
    def __init__(self):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "X"}

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()


#b = Board()
#print(b)

