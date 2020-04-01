from domain.order import Order

class OrderRepository:

    def __init__(self, fileName="orders.txt"):
        self.__data = []
        self.__fName = fileName
        self.__loadFromFile()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        r = ""
        for order in self.__data:
            r += str(order) + "\n"

        return r

    def add(self, order):
        '''
        INPUT: an order
        OUTPUT: the order is added to the data base of orders
        '''
        self.__data.append(order)
        self.__storeToFile()

    def getAll(self):
        '''
        OUTPUT: return all orders from the data base
        '''
        return self.__data

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                tok = line.split(",")
                order = Order(int(tok[0]), int(tok[1]))
                OrderRepository.add(self, order)
                line = f.readline().strip()
        except IOError:
            raise ValueError("Something went wrong.")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        orders = OrderRepository.getAll(self)
        for ord in orders:
            ordf = str(ord.getDriverId()) + "," + str(ord.getDistance())
            ordf = ordf + "\n"
            f.write(ordf)
        f.close()

class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


