from board import Board

class Game():
    def __init__(self):
        self.board = Board()

    def moveHuman(self, r, c):
        s = "X"
        self.board.move(r, c, s)

    def moveComputer(self, r, c):
        s = "O"
        self.board.move(r, c, s)

    def isWon(self, r, c, s):
        if c >= 3 and self._goLeft(r, c, s):
            return True

        if c <= 3 and self._goRight(r, c, s):
            return True

        if r >= 3 and self._goUp(r, c, s):
            return True

        if r <= 2 and self._goDown(r, c, s):
            return True

        return False

    def _goLeft(self, r, c, s):
        if self.board.getValue(r, c - 1) == s:
            if self.board.getValue(r, c - 2) == s:
                if self.board.getValue(r, c - 3) == s:
                    return True
        return False
        
    def _goRight(self, r, c, s):
        if self.board.getValue(r, c + 1) == s:
            if self.board.getValue(r, c + 2) == s:
                if self.board.getValue(r, c + 3) == s:
                    return True
        return False

    def _goUp(self, r, c, s):
        if self.board.getValue(r - 1, c) == s:
            if self.board.getValue(r - 2, c) == s:
                if self.board.getValue(r - 3, c) == s:
                    return True
        return False

    def _goDown(self, r, c, s):
        if self.board.getValue(r + 1, c) == s:
            if self.board.getValue(r + 2, c) == s:
                if self.board.getValue(r + 3, c) == s:
                    return True
        return False


#g = Game()
#g.moveHuman(1, 1)
#g.moveComputer(2, 2)
#print(g.board)
