from repository.studentRepo import StudentRepository
import pickle


class StudentPickleFileRepository(StudentRepository):
    def __init__(self, fileName = "students.pickle"):
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

    def update(self, oldStudent, newStudent):
        StudentRepository.update(self, oldStudent, newStudent)
        self.__storeToFile()

    def __loadFromFile(self):
        f = open(self.__fName, "rb")

        try:
            l = pickle.load(f)
            for s in l:
                StudentRepository.add(self, s)
        except EOFError:
            self._data = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()
