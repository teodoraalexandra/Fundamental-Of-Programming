class Driver:
    def __init__(self, driverId, name):
        self.__driverId = driverId
        self.__name = name

    def __eq__(self, driver):
        return self.__driverId == driver.__driverId and self.__name == driver.__name

    def getDriverId(self):
        return self.__driverId

    def getName(self):
        return self.__name

    def setDriverId(self, a):
        self.__driverId = a

    def setName(self, b):
        self.__name = b

    def __str__(self):
        r = ''
        r += str(self.__driverId)
        r += ' '
        r += str(self.__name)

        return r

