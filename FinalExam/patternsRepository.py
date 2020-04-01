from pattern import Pattern

class Patterns():
    def __init__(self, fileName="patterns.txt"):
        self.__data = []
        self.__fName = fileName
        self.__loadFromFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(",")
                pattern = Pattern(tok[1], tok[2], tok[3], tok[4])
                Patterns.add(self, pattern)
                line = f.readline().strip()
        except IOError:
            raise ValueError("Something went wrong.")
        finally:
            f.close()
