class Grade:
    def __init__(self, disciplineId, studentId, value):
        self.__disciplineId = disciplineId
        self.__studentId = studentId
        self.__value = value

    def __eq__(self, grade):
        return self.__disciplineId == grade.__disciplineId and self.__studentId == grade.__studentId and self.__value == grade.__value

    def getDisciplineId(self):
        return self.__disciplineId

    def getStudentId(self):
        return self.__studentId

    def getValue(self):
        return self.__value

    def __str__(self):
        r = ''
        if self.__disciplineId > 0:
            r += str(self.__disciplineId)
        r += ' '

        if self.__studentId > 0:
            r += str(self.__studentId)
        r += ' '

        if self.__value > 0 and self.__value < 11:
            r += str(self.__value)

        return r

