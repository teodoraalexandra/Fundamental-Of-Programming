from repository.gradeRepo import GradeRepository
from domain.grade import Grade


class GradeCSVFileRepository(GradeRepository):
    def __init__(self, fileName = "grades.txt"):
        GradeRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def add(self, grade):
        GradeRepository.add(self, grade)
        self.__storeToFile()

    def remove(self, grade):
        GradeRepository.remove(self, grade)
        self.__storeToFile()

    def removeAll(self):
        GradeRepository.removeAll(self)
        self.__storeToFile()

    def getAll(self):
        return GradeRepository.getAll(self)

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(" ")
                grade = Grade(int(tok[0]), int(tok[1]), int(tok[2]))
                GradeRepository.add(self, grade)
                line = f.readline().strip()
            f.close()
        except IOError:
            raise ValueError("Something went wrong.")

    def __storeToFile(self):
        f = open(self.__fName, "w")
        grades = GradeRepository.getAll(self)
        for gr in grades:
            strf = str(gr.getDisciplineId()) + " " + str(gr.getStudentId()) + " " + str(gr.getValue())
            strf = strf + "\n"
            f.write(strf)
        f.close()
