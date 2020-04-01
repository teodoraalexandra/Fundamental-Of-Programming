from domain.board import Square

class UI:
    def __init__(self, g):
        self._game = g

    def _readMove(self):
        while True:
            try:
                col = int(input("Enter the column: "))
                return Square(5, col)
            except Exception as e:
                print("Invalid move!")

    def start(self):
        ok = True
        while ok:
            try:
                b = self._game.board

                playerMove = True
                while b.isWon() == False and b.isTie() == False:
                    if playerMove:
                        print(b)
                        move = self._readMove()
                        self._game.moveHuman(move)
                    else:
                        self._game.moveComputer()
                    playerMove = not playerMove

                print("Game over!")
                print(b)
                if b.isWon():
                    if playerMove == True:
                        print("Computer wins!")
                        ok = False
                    else:
                        print("Player wins!")
                        ok = False
                else:
                    print("It's a tie!")
                    ok = False

            except Exception as me:
                print(me)

