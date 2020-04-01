class Discipline:
    def __init__(self, disciplineId, name):
        self.__disciplineId = disciplineId
        self.__name = name

    def __eq__(self, discipline):
        return self.__disciplineId == discipline.__disciplineId and self.__name == discipline.__name

    def getDisciplineId(self):
        return self.__disciplineId

    def getName(self):
        return self.__name

    def setDisciplineId(self, a):
        self.__disciplineId = a

    def setName(self, b):
        self.__name = b

    def __str__(self):
        r = ''
        if self.__disciplineId > 0:
            r += str(self.__disciplineId)
        r += ' '
        r += str(self.__name)

        return r
