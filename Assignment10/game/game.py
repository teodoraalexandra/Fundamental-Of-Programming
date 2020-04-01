from domain.board import Board
from random import choice

class Game:
    def __init__(self):
        self._board = Board()

    @property
    def board(self):
        return self._board

    def moveHuman(self, square):
        self.board.move(square, 'Y')

    def moveComputer(self):
        options = self.board.getEmptySquares()
        if len(options) == 0:
            raise GameException("Board is full!")

        '''
        Try to win !!!
        '''
        for option in options:
            '''
            1. create board copy
            2. try move
            3. check for win
            '''
            b = self.board.copy()
            b.move(option, 'R')

            if b.isWon() == True:
                self.board.move(option, 'R')
                return

        '''
        Prevent human win!
        '''
        for option in options:
            '''
            1. create board copy
            2. try move
            3. check for win
            '''
            b = self.board.copy()
            b.move(option, 'Y')

            if b.isWon() == True:
                self.board.move(option, 'R')
                return

        self.board.move(choice(options), 'R')


class GameException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

