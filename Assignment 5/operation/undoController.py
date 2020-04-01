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
            raise ControllerException("No undo steps available!")

        self._operations[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index + 1 >= len(self._operations):
            raise ControllerException("No redo steps available!")

        self._index += 1
        self._operations[self._index].redo()

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
        self._func = func
        self._params = params

    def call(self):
        self._func(*self._params)

class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
