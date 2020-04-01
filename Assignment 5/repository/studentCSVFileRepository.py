from repository.studentRepo import StudentRepository
from domain.student import Student


class StudentCSVFileRepository(StudentRepository):
    def __init__(self, fileName = "students.txt"):
        StudentRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def add(self, student):
        StudentRepository.add(self, student)
        self.__storeToFile()

    def remove(self, student):
        StudentRepository.remove(self, student)
        self.__storeToFile()

    def removeAll(self):
        StudentRepository.removeAll(self)
        self.__storeToFile()

    def getAll(self):
        return StudentRepository.getAll(self)

    def update(self, oldStudent, newStudent):
        StudentRepository.update(self, oldStudent, newStudent)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(" ")
                student = Student(int(tok[0]), tok[1])
                StudentRepository.add(self, student)
                line = f.readline().strip()
        except IOError:
            raise ValueError("Something went wrong.")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        students = StudentRepository.getAll(self)
        for st in students:
            strf = str(st.getStudentId()) + " " + str(st.getName())
            strf = strf + "\n"
            f.write(strf)
        f.close()
