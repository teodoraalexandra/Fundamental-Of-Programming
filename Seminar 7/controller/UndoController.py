class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1

    def addOperation(self, operation):
        self._operations = self._operations[:self._index + 1]
        self._index += 1
        self._operations.append(operation)

    def undo(self):
        if self._index < 0:
            return False

        self._operations[self._index].undo()
        self._index -= 1
        return True

    def redo(self):
        if self._index >= len(self._operations):
            return False

        self._index += 1
        self._operations[self._index].redo()
        return True

class CascadeOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for o in self._operations:
            o.undo()

    def redo(self):
        for o in self._operations:
            o.redo()

class Operation:
    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction

    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()

class FunctionCall:
    def __init__(self, func, *params):
        self._func =func
        self._params = params

    def call(self):
        self._func(*self._params)

def a(a,b,c):
    print(a)
    print(b)
    print(c)

f = FunctionCall(a, '1', '2', '3')
f.call()
