from operation.undoController import *
from domain.discipline import Discipline

class DisciplineController:
    def __init__(self, repoD):
        self.__repoD = repoD

    def __str__(self):
        return str(self.__repoD)

    def addDiscipline(self, discipline):
        self.__undo = self.__repoD.getAll()[:]
        self.__repoD.add(discipline)

    def removeDiscipline(self, discipline):
        self.__undo = self.__repoD.getAll()[:]
        self.__repoD.remove(discipline)

    def removeAll(self, discipline):
        self.__undo = self.__repoD.getAll()[:]
        while self.__repoD.find(discipline) > -1:
            index = self.__repoD.find(discipline)
            self.__repoD.remove(index)

    def updateDiscipline(self, oldDiscipline, newDiscipline):
        self.__undo = self.__repoD.getAll()[:]
        self.__repoD.update(oldDiscipline, newDiscipline)

    def getAll(self):
        return self.__repoD.getAll()

    def checkId(self, discipline):
        for i in self.getAll():
            if i.getDisciplineId() == discipline.getDisciplineId():
                return True

    def undo(self):
        if len(self.__undo) == 0:
            raise ControllerException("No undo steps available!")

        self.__repoD.removeAll()
        for i in self.__undo:
            self.__repoD.add(i)
        self.__undo.clear()

class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message





