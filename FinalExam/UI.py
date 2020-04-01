from board import Board
from pattern import Block
from pattern import Tub
from pattern import Blinker
from pattern import Beacon
from pattern import Spaceship


class UI:
    def __init__(self):
        self._data = []

    def start(self):
        ok = True
        try:
            while ok:
                option = input("Place block/ tub/ blinker/ beacon/ spaceship: ").split()
                if option[0] == "place":
                    if option[1] == "block":
                        b = Block()
                        print(b)
                    elif option[1] == "tub":
                        t = Tub()
                        print(t)
                    elif option[1] == "blinker":
                        b = Blinker()
                        print(b)
                    elif option[1] == "beacon":
                        b = Beacon()
                        print(b)
                    elif option[1] == "spaceship":
                        s = Spaceship()
                        print(s)
                    else:
                        raise ValueError("This pattern does not exist")
                elif option[0] == "tick":
                    pass
                elif option[0] == "save":
                    pass
                elif option[0] == "0":
                    ok = False
                else:
                    raise ValueError("Keyword wrong.")
        except Exception as me:
            print(me)

    def place(self, row, col):
        self.board.place(row, col, 'X')


ui = UI()
ui.start()







