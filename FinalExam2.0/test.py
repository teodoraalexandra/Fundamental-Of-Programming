from ui import UI

def test():
    there = [3, 3]
    blingon = [[3, 5], [2, 2,], [1, 4]]
    ui = UI()
    ui.wrap(3, 4, there, blingon)
    ui.game.board.move(3, 3, ' ')
    ui.game.board.move(3, 4, 'E')

test()


