from domain.driver import Driver

class DriverRepository:

    def __init__(self, fileName="drivers.txt"):
        self.__data = []
        self.__fName = fileName
        self.__loadFromFile()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        r = ""
        for driver in self.__data:
            r += str(driver) + "\n"

        return r

    def add(self, driver):
        '''
        INPUT: a driver
        OUTPUT: the driver is added to the data base of drivers
        '''
        self.__data.append(driver)
        self.__storeToFile()

    def getAll(self):
        '''
        OUTPUT: return all drivers from the data base
        '''
        return self.__data

    def checkId(self, id):
        '''
        INPUT: id
        OUTPUT: true if the driver with the given id exists, false otherwise
        '''
        for i in self.getAll():
            if i.getDriverId() == id:
                return True

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(",")
                driver = Driver(int(tok[0]), tok[1])
                DriverRepository.add(self, driver)
                line = f.readline().strip()
        except IOError:
            raise ValueError("Something went wrong.")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        drivers = DriverRepository.getAll(self)
        for dr in drivers:
            drs = str(dr.getDriverId()) + "," + str(dr.getName())
            drs = drs + "\n"
            f.write(drs)
        f.close()

class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


