class Order:
    def __init__(self, driverId, distance):
        self.__driverId = driverId
        self.__distance = distance

    def __eq__(self, order):
        return self.__driverId == order.__driverId and self.__distance == order.__distance

    def getDriverId(self):
        return self.__driverId

    def getDistance(self):
        return self.__distance

    def setDriverId(self, a):
        self.__driverId = a

    def setDistance(self, b):
        self.__distance = b

    def __str__(self):
        r = ''
        r += str(self.__driverId)
        r += ' '
        r += str(self.__distance)

        return r