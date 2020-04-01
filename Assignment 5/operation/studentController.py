from operation.undoController import *
from domain.student import Student

class StudentController:
    def __init__(self, repoS, undoController):
        self.__repoS = repoS
        self.__undoController = undoController

    def __str__(self):
        return str(self.__repoS)

    def addStudent(self, student):
        self.__repoS.add(student)

    def removeStudent(self, student):
        self.__repoS.remove(student)

    def removeAll(self):
        self.__undo = self.__repoS.getAll()[:]
        self.__repoS.clear()

    def updateStudent(self, oldStudent, newStudent):
        self.__undo = self.__repoS.getAll()[:]
        self.__repoS.update(oldStudent, newStudent)

    def getAll(self):
        return self.__repoS.getAll()

    def checkId(self, student):
        for i in self.getAll():
            if i.getStudentId() == student.getStudentId():
                return True

    def undo(self):
        if len(self.__undo) == 0:
            raise ControllerException("No undo steps available!")

        self.__repoS.removeAll()
        for i in self.__undo:
            self.__repoS.add(i)
        self.__undo.clear()

class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
