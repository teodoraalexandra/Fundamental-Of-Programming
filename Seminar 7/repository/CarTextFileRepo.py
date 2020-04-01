from repository.Repository import Repository
from repository.RepositoryException import RepositoryError
from domain.Car import Car

class CarTextFileRepo(Repository):
    def __init__(self, fileName = "cars.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def store(self, obj):
        Repository.store(self, obj)
        self._saveFile()

    def _saveFile(self):
        f = open(self._fileName, "w")
        for c in self.getAll():
            f.write(str(c.id) + "," + c.license + "," + c.make + "," + c.model + "\n")
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline()
            while len(line) > 2:
                tok = line.split(",")

                car = Car(int(tok[0]), tok[1], tok[2], tok[3].strip())
                Repository.store(self, car)

                line = f.readline()
        except IOError as e:
            raise RepositoryError("Cannot load file " + str(e))
        finally:
            print("Finally")
            f.close()
