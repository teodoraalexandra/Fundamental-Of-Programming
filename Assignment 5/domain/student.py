class Student:
    def __init__(self, studentId, name):
        self.__studentId = studentId
        self.__name = name

    def __eq__(self, student):
        return self.__studentId == student.__studentId and self.__name == student.__name

    def getStudentId(self):
        return self.__studentId

    def getName(self):
        return self.__name

    def setStudentId(self, a):
        self.__studentId = a

    def setName(self, b):
        self.__name = b

    def __str__(self):
        r = ''
        if self.__studentId > 0:
            r += str(self.__studentId)
        r += ' '
        r += str(self.__name)

        return r
