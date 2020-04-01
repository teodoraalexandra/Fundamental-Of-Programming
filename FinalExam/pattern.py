from texttable import Texttable


class Block:
    def __init__(self, fileName = "patterns.txt"):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]
        self.__fName = fileName

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "X"}

        self.place(0, 0, 1)
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 1, 1)
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()
        #self.__storeToFile()


    def __storeToFile(self):
        f = open(self.__fName, "w")
        d = self.__data
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write("\n")
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                f.write(str(d[i][j]))
        f.close()

class Tub:
    def __init__(self, fileName = "patterns.txt"):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]
        self.__fName = fileName

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def isAlive(self):
        d = self.__data
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                if d[i][j] == 0:
                    ok = False
                else:
                    ok = True
        return ok


    def __str__(self):
        '''
        t = Texttable()
        d = {0: " ", 1: "X"}

        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()
        '''
        self.__storeToFile()


    def __storeToFile(self):
        f = open(self.__fName, "w")
        d = self.__data
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write("\n")
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                f.write(str(d[i][j]))
        f.close()


class Blinker:
    def __init__(self, fileName = "patterns.txt"):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]
        self.__fName = fileName

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def __str__(self):
        '''
        t = Texttable()
        d = {0: " ", 1: "X"}

        self.place(1, 0, 1)
        self.place(1, 1, 1)
        self.place(1, 2, 1)
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()
        '''
        self.__storeToFile()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        d = self.__data
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write("\n")
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                f.write(str(d[i][j]))
        f.close()

class Beacon:
    def __init__(self, fileName = "patterns.txt"):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]
        self.__fName = fileName

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "X"}

        self.place(0, 0, 1)
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 1, 1)
        self.place(2, 2, 1)
        self.place(2, 3, 1)
        self.place(3, 2, 1)
        self.place(3, 3, 1)
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()
        #self.__storeToFile()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        d = self.__data
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write("\n")
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                f.write(str(d[i][j]))
        f.close()

class Spaceship:
    def __init__(self, fileName = "patterns.txt"):
        self.__data = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]
        self.__fName = fileName

    def place(self, row, col, pattern):
        if row not in [0, 1, 2, 3, 4, 5, 6, 7] or col not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Move outside board!")

        d = self.__data
        d[row][col] = pattern

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "X"}

        self.place(0, 1, 1)
        self.place(1, 2, 1)
        self.place(2, 0, 1)
        self.place(2, 1, 1)
        self.place(2, 2, 1)
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            lst = self.__data[i][:]
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                lst[j] = d[lst[j]]
            t.add_row(lst)
        return t.draw()
        #self.__storeToFile()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        d = self.__data
        self.place(0, 1, 1)
        self.place(1, 0, 1)
        self.place(1, 2, 1)
        self.place(2, 1, 1)

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            f.write("\n")
            for j in [0, 1, 2, 3, 4, 5, 6, 7]:
                f.write(str(d[i][j]))
        f.close()
