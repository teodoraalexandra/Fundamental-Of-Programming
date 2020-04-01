class Reservation:
    def __init__(self, id, number, name, guests, arrival, departure):
        self.__id = id
        self.__number = number
        self.__name = name
        self.__guests = guests
        self.__arrival = arrival
        self.__departure = departure

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def guests(self):
        return self.__guests

    @property
    def arrival(self):
        return self.__arrival

    @property
    def departure(self):
        return self.__departure

    def __str__(self):
        r = ""
        r += str(self.__id)
        r += ' '
        r += str(self.__number)
        r += ' '
        r += str(self.__name)
        r += ' '
        r += str(self.__guests)
        r += ' '
        r += str(self.__arrival)
        r += ' '
        r += str(self.__departure)

        return r
