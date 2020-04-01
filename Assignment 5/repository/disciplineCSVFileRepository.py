from repository.disciplineRepo import DisciplineRepository
from domain.discipline import Discipline


class DisciplineCSVFileRepository(DisciplineRepository):
    def __init__(self, fileName = "disciplines.txt"):
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

    def getAll(self):
        return DisciplineRepository.getAll(self)

    def update(self, oldDiscipline, newDiscipline):
        DisciplineRepository.update(self, oldDiscipline, newDiscipline)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(" ")
                discipline = Discipline(int(tok[0]), tok[1])
                DisciplineRepository.add(self, discipline)
                line = f.readline().strip()
            f.close()
        except IOError:
            raise ValueError("Something went wrong.")

    def __storeToFile(self):
        f = open(self.__fName, "w")
        disciplines = DisciplineRepository.getAll(self)
        for ds in disciplines:
            strf = str(ds.getDisciplineId()) + " " + str(ds.getName())
            strf = strf + "\n"
            f.write(strf)
        f.close()
