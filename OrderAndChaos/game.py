from texttable import *

class Board:
    def __init__(self):
        self.data = [[" "]*6 for i in range (6)]

    def draw_board(self):
        t = Texttable()
        for i in range(6):
            t.add_row(self.data[i])
        t.header(["0","1","2","3","4","5"])
        return t.draw()

    def move(self, r,c,s):
        '''
        This function "draws" the symbol from the input at the position
        data[r][c]
        '''
        self.data[r][c] = s#
    def set_value(self,i,j,val):
        if val == "-":
            self.data[i][j] = " "
        elif val == "x":
            self.data[i][j] = "X"
        elif val == "o":
            self.data[i][j] = "O"
    def get_folder_value(self,i,j):
        if self.data[i][j] == " ":
            return "-"
        elif self.data[i][j] == "X":
            return  "x"
        elif self.data[i][j] == "O":
            return "o"


def test_draw():
        b = Board()
        print(b.draw_board())

# test_draw()

class Game:
    def __init__(self):
        '''
        Both the player and the computer will have separate boards
        The moves made on the player's board will be made in the exact same manner on the computer's
        Separately, the computer's board adds in every possible case the symbol to its boards, and checks whether the
        player could win by making that particular move
        '''
        self.play = Board()
        self.computer = Board()

    def move_human(self, r,c,s):
        self.play.move(r, c, s)

        #if self.check_victory(r,c,s) == True:


    def check_victory(self, r, c, s):
        '''
        This function checks whether the player has won or not yet
        To be more efficient, it will start checking around the last move made by the player, since it's the only case in which
        the player could have won
        '''
        '''
        Count how many identical symbols are on the same line, diagonal or row with the last 
        element added
        '''

        left_right = up_down = 0
        lu_rd = ld_ru = 0   #left-up, right-down ...
        left_right += self.goLeftRight(r,c,s)
        up_down += self.goUpDown(r,c,s)
        lu_rd += self.goLU_RD(r,c,s)
        ld_ru += self.goLD_RU(r,c,s)

        if up_down >=4 :
            return True
        if left_right >=4:
            return True
        if lu_rd >=4:
            return True
        if ld_ru >=4:
            return True
        return False


    def check_full_board(self):
        '''
        Checks whether the board is full
        '''
        for i in range(6):
            for j in range(6):
                if self.play.data[i][j] == " ":
                    return False
        return True

    def check_possible_win(self):
        for i in range(6):
            for j in range(6):
                if self.play.data[i][j] == " ":
                    if self.check_victory(i,j,"X") == True:
                        return i,j,"O"
                    elif self.check_victory(i,j,"O") == True:
                        return i,j,"X"
        return None, None, None

    def non_empty(self, r, c, s):
        '''
        Checks if the given position is empty or if the values are valid (!= None)
        '''
        if r == None or c == None or s == None:
            return True
        if self.play.data[r][c] != " ":
            return True
        return False

    def goLeftRight(self, r, c, s):
        '''
        count how many identical symbols are on the same line
        '''
        same = 0
        i = c - 1
        while i >=0 and self.play.data[r][i] == s :
            same += 1
            i -= 1

        i = c+1
        while i <= 5 and self.play.data[r][i] == s :
            same += 1
            i+= 1
        return same
    def goUpDown(self,r,c,s):
        same = 0
        # i = c-1
        i = r -1
        while i >= 0 and self.play.data[i][c] == s:
            same += 1
            i -= 1

        i = r + 1
        while i <= 5 and self.play.data[i][c] == s:
            same += 1
            i += 1
        return same

    def goLU_RD(self, r, c, s):
        i = r-1
        j = c-1
        same = 0
        '''
        Checks the diagonals
        '''
        while i >=0 and j >=0 and self.play.data[i][j] == s:
            i -= 1
            j -= 1
            same += 1
        i = r+1
        j = c+1
        while i <= 5 and j <= 5 and self.play.data[i][j] == s:
            i += 1
            j += 1
            same += 1
        return same

    def goLD_RU(self, r, c, s):
        i = r+1
        j = c-1
        same = 0
        '''
        Checks the diagonals
        '''
        while i <= 5 and j >=0 and self.play.data[i][j] == s:
            i += 1
            j -= 1
            same += 1
        i = r-1
        j = c+1
        while i >= 0 and j <= 5 and self.play.data[i][j] == s:
            i -= 1
            j += 1
            same += 1
        return same

# game = Game()
# print(game.check_full_board())

def test_goLR():
    game2 = Game()

    fd = open("test1.txt", "r")
    #game2.play.get_folder_value()
    line = fd.readline()
    while len(line):
        # line = fd.readline()
        for i in range(6):
            for j in range(6):
                game2.play.get_folder_value(i,j)
        line = fd.readline()
    fd.close()

    print(game2.play.draw_board())
# test_goLR()