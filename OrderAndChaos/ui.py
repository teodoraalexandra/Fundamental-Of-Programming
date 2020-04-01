from game import Game
from random import *

class UI:
    def __init__(self):
        self.game = Game()
        self.game_over = False

    def choose_what_to_do(self):
        print("Will you start a new game or load a saved one ?")
        print(">>1: Start a new game")
        print(">>2: Load a saved one")
        print(">>0: Exit")
        i = input(":")
        if i == "1":
            self.new_game()
        elif i =="2":
            self.load_game("input.txt")
        elif i == "0":
            self._end_game()
        else:
            print("Invalid input. Try again!")
            self.choose_what_to_do()
    def print_input(self):
        print("Stop here and save the game?")
        print(">>0: NO")
        print(">>1: YES")
        i = input(":")
        if i == "1":
            self.save_game()
            self._end_game()
            return
        print("Choose your next move: ")
        r = input("\t1>> row: ")
        c = input("\t2>> column: ")
        s = input("\t3 >>symbol: ")
        e = self.check_inputs(r,c,s)
        if len(e):
            print(e)
            print("\nInvalid inputs! try again:\n")
            self.print_input()
        else:
            print("let's try here", e, "in line 44")
            r = int(r)
            c = int(c)
            self.player_move(r,c,s)
    def check_inputs(self,r,c,s):
        '''
        The rows will be indexed from 0 to 5
        :param r: row
        :param c: column
        :param s: symbol
        :return: a list of (possible) errors
        If the position chosen is non_empty, signals an error
        '''
        e = []
        try:
            r = int(r)
            c = int(c)
        except ValueError:
            e.append("The inputs must be numbers!")
        if r not in range(6):
            e.append("The rows must be in range 0-5!")
            return e
        if c not in range (6):
            e.append("The columns must be in range 0-5")
            return e
        if s not in ["X", "O"]:
            e.append("The symbol must be O or X")
        if self.game.play.data[r][c] != " ":
            e.append("Nonempty space!")
        return e

    def player_move(self, r, c, s):
        '''
        Makes the player's move
        If the player won, displays a "victory" message
        '''
        self.game.play.move(r, c, s)
        print(self.game.play.draw_board())
        # self.game.computer.move(r,c,s)  #the computer makes the same moves in his board
        if self.game.check_victory(r,c,s):
            print("\n\tYou won!")
            return
        elif self.game.check_full_board():
            print("You lost! :(\nBetter luck next time!")
        else:
            '''
            Checks if the player could win by making the next move
            If so, it return row, column and symbol of 
            '''
            r,c,s = self.game.check_possible_win()

            if r != None:
                self.game.play.move(r, c, s)    #make the move that prevents pla player's victory
                # self.game.computer.move(r,c,s)
                print(self.game.play.draw_board())
            else:
                while self.game.non_empty(r,c,s) :
                    r = choice([0,1,2,3,4,5])
                    c = choice([0,1,2,3,4,5])
                    s = choice(["X","O"])
                self.game.play.move(r, c, s)
                # self.game.computer.move(r,c,s)
                print(self.game.play.draw_board())
                if self.game.check_victory(r,c,s):
                    print("\nYou won!")
                    self._end_game()
                elif self.game.check_full_board():
                    print("You lost!")
                    self._end_game()


    def new_game(self):
        # self.game = Game()
        print(self.game.play.draw_board())
        while self.game_over == False:
            self.print_input()

    def load_game(self, filename):
        fd = open(filename, "r")
        line = fd.readline()
        i = 0
        while len(line) > 0:
            for j in range(len(line)):
                self.game.play.set_value(i,j,line[j])
            i += 1
            line = fd.readline()
        print(self.game.play.draw_board())
        fd.close()
        while True:
            self.print_input()
    def save_game(self):
        fd = open("input.txt", "w")
        for i in range(6):
            for j in range(6):
                fd.write(self.game.play.get_folder_value(i,j))
            fd.write("\n")
        fd.close()
        self._end_game()

    def _end_game(self):
        self.game_over == True

ui = UI()
ui.choose_what_to_do()


def tests():
    '''
    Check if the computer is able to stop the player and if
    the computer's moves are validated
    Will use 3 test folders for that
    '''
    # test_game = Game()
    test_ui = UI()
    test_ui.load_game("test1.txt")
    assert test_ui.game.check_full_board() == True  #it works
    # now let's check if selecting an already marked box will result in any difference
    # spoiler alert, it won't
    test_ui2 = UI()
    test_ui2.load_game("test2.txt")
    test_ui2.game.move_human(0,0,"X")    #supposibly it will turn the "O" into "X"
                                        #respectively the "o" in the file into "x"
    assert test_ui.game.play.get_folder_value(0,0) == "o"

    #now let's check if the computer stops the player's move
    test_ui3 = UI()
    test_ui3.load_game("test3.txt")
    test_ui3.player_move(1,1,"X")   #after the player's move, the computer automatically
                                    #places the opposite sign in position (0,0)
    assert test_ui3.game.play.get_folder_value(0,0) == "o"
tests()
