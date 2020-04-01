from domain import Game


class UI():
    def __init__(self):
        self.game = Game()

    def _printMenu(self):
        print("\t1. Start game")
        print("\t2. Wrap")
        print("\t3. Fire")
        print("\t4. Cheat")
        print("\t0. Exit")

        i = input(":")
        if i == "1":
            self.game.placeStars()
            self.game.placeUSS()
            self.game.placeBlingon()
            print(self.game.board)
            self._printMenu()
        elif i == "2":
            self._readInput(i)
            print(self.game.board)
            self._printMenu()
        elif i == "3":
            self._readInput(i)
            print(self.game.board)
            self._printMenu()
        elif i == "4":
            pass
        elif i == "0":
            return
        else:
            print("Invalid command.")
            self._printMenu()
            return

    def _readInput(self, i):
        try:
            r = int(input("Enter the row: "))
            c = int(input("Enter the column: "))

            if r < 0 or r > 7:
                print("You enter an invalid row")
                self._readInput(i)
                return
            if c < 0 or c > 7:
                print("You enter an invalid column")
                self._readInput(i)
                return

            if i == "2":
                self._moveShip(r, c)
                return
            elif i == "3":
                self._fireShip(r, c)
                return

        except ValueError:
            print("Something went wrong")
            self._printMenu()

    def _fireShip(self, r, c):
        there = self._findUSS()
        blingon = self._findBlingon()

        if self.game.board.getValue(r, c) != "B":
            print("The blingon is not on these coordinates.")
            self._printMenu()

        if there[0] == r + 1 and there[1] == c + 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r + 1 and there[1] == c:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r + 1 and there[1] == c - 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r and there[1] == c - 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r and there[1] == c + 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r - 1 and there[1] == c + 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r - 1 and there[1] == c:
            print("You fire the enemy!")
            self.game.placeBlingon()

        elif there[0] == r - 1 and there[1] == c - 1:
            print("You fire the enemy!")
            self.game.placeBlingon()

        else:
            print("The Blingon is not near you")

    def _moveShip(self, r, c):
        there = self._findUSS()
        blingon = self._findBlingon()
        self.wrap(r, c, there, blingon)

    def wrap(self, r, c, there, blingon):
        if there[0] == r:
            if blingon[0] == [there[0], c] or blingon[1] == [there[0], c] or blingon[2] == [there[0], c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(there[0], c, 'E')

        elif there[1] == c:
            if blingon[0] == [r, there[1]] or blingon[1] == [r, there[1]] or blingon[2] == [r, there[1]]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, there[1], 'E')

        elif there[0] + 1 == r and there[1] + 1 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 2 == r and there[1] + 2 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 3 == r and there[1] + 3 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 4 == r and there[1] + 4 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 5 == r and there[1] + 5 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 6 == r and there[1] + 6 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] + 7 == r and there[1] + 7 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 1 == r and there[1] - 1 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 2 == r and there[1] - 2 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 3 == r and there[1] - 3 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 4 == r and there[1] - 4 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 5 == r and there[1] - 5 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 6 == r and there[1] - 6 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        elif there[0] - 7 == r and there[1] - 7 == c:
            if blingon[0] == [r, c] or blingon[1] == [r, c] or blingon[2] == [r, c]:
                print("You land on the enemy ship!")
                self.gameOver()
            else:
                self.game.board.move(there[0], there[1], ' ')
                self.game.board.move(r, c, 'E')

        else:
            print("You can not move your ship!")

    def _findBlingon(self):
        there = []
        for i in range(8):
            for j in range(8):
                if self.game.board.getValue(i, j) == "B":
                    there.append([i,j])
        return there

    def _findUSS(self):
        there = []
        for i in range(8):
            for j in range(8):
                if self.game.board.getValue(i, j) == "E":
                    there.append(i)
                    there.append(j)
        return there

    def gameOver(self):
        exit()


class GameException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


ui = UI()
ui._printMenu()
