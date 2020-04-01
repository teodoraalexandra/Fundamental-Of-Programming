from repository.disciplineRepo import DisciplineRepository
import pickle


class DisciplinePickleFileRepository(DisciplineRepository):
    def __init__(self, fileName = "disciplines.pickle"):
        DisciplineRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def add(self, discipline):
        DisciplineRepository.add(self, discipline)
        self.__storeToFile()

    def remove(self, discipline):
        DisciplineRepository.remove(self, discipline)
        self.__storeToFile()

    def removeAll(self):
        DisciplineRepository.removeAll(self)
        self.__storeToFile()

    def update(self, oldDiscipline, newDiscipline):
        DisciplineRepository.update(self, oldDiscipline, newDiscipline)
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
