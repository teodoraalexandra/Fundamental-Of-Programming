class OrderController:
    def __init__(self, repoO):
        self.__repoO = repoO

    def __str__(self):
        return str(self.__repoO)

    def addOrder(self, order):
        self.__repoO.add(order)

    def getAll(self):
        return self.__repoO.getAll()

    def checkId(self, order):
        for i in self.getAll():
            if i.getDriverId() == order.getDriverId():
                return True

    def checkList(self, id):
        for i in self.getAll():
            if i.getDriverId() == id:
                return True

class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

