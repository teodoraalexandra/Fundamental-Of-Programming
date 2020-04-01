from repository.gradeRepo import GradeRepository
import pickle


class GradePickleFileRepository(GradeRepository):
    def __init__(self, fileName = "grades.pickle"):
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

    def __loadFromFile(self):
        f = open(self.__fName, "rb")

        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()
