class DriverController:
    def __init__(self, repoD):
        self.__repoD = repoD

    def __str__(self):
        return str(self.__repoD)

    def addDriver(self, driver):
        self.__repoD.add(driver)

    def getAll(self):
        return self.__repoD.getAll()

    def checkId(self, driverId):
        return self.__repoD.checkId(driverId)


class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

