from game import Game


class UI():
    def __init__(self):
        self.game = Game()

    def _printMenu(self):
        print("\t1. Start new game")
        print("\t2. Load a saved game")
        print("\t0. Exit")
        print("\n")

        i = int(input(":"))
        if i == 1:
            self.new_game()
        elif i == 2:
            self.load_new_game("input.txt")
        elif i == 0:
            return
        else:
            print("Invalid command!")

    def new_game(self):
        print(self.game.board)
        self.input_commands()

    def load_new_game(self, fileName):
        try:
            fd = open(fileName, 'r')
            data = []
            line = fd.readline()
            while len(line):
                for i in range(len(line)):
                    if line[i] != '\n':
                        data.append(line[i])
                line = fd.readline()
            fd.close()
            index = 0
            for i in range(6):
                for j in range(6):
                    if data[index] == "-":
                        data[index] = ' '

                    elif data[index] == "x":
                        data[index] = 'X'

                    elif data[index] == "o":
                        data[index] = 'O'

                    self.game.board.move(i, j, data[index])
                    index += 1

            print(self.game.board)
            self.input_commands()

        except Exception as me:
            print(me)

    def save_game(self, fileName):
        fd = open(fileName, 'w')
        for i in range(6):
            for j in range(6):
                square = self.game.board.getValue(i, j)
                if square == ' ':
                    square = '-'

                if square == 'X':
                    square = 'x'

                if square == 'O':
                    square = 'o'

                fd.write(square)
            fd.write("\n")
        fd.close()


    def input_commands(self):
        r = input("Enter row: ")
        if r == "save":
            self.save_game("input.txt")
            return
        c = input("Enter column: ")

        not_valid = self.check_input(r, c)

        if len(not_valid) != 0:
            print(self.check_input(r, c))
            self.input_commands()
            return

        r = int(r)
        c = int(c)
        self.game.moveHuman(r, c)
        if self.game.isWon():
            print("You won")
            return
        else:
            self.game.moveComputer()
            print(self.game.board)
            if self.game.isWon():
                print("Computer won")
                return
            self.input_commands()

    def check_input(self, r, c):
        e = []
        try:
            r = int(r)
            c = int(c)
        except ValueError:
            e.append("Row and column must be integers")
            return e

        r = int(r)
        c = int(c)
        if r > 5 or r < 0 or c > 5 or c < 0:
            e.append("Move outside board")
            return e

        if not self.game.board.getEmptySquare(r, c):
            e.append("Not an empty square")
        return e


ui = UI()
ui._printMenu()
