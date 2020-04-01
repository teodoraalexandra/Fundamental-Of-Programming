from controller.CarRentalException import CarRentalException
from domain.Rental import Rental

class RentalController:
    """
    Controller for rental operations
    """
    def __init__(self, validator, rentalRepo, carRepo, clientRepo):
        self.__validator = validator
        self.__repository = rentalRepo
        self.__carRepo = carRepo
        self._cliRepo = clientRepo

    def createRental(self, rentalId, client, car, start, end):
        rental = Rental(rentalId, start, end, client, car)
        self.__validator.validate(rental)
        
        '''
        Check the car's availability for the given period 
        '''
        if self.isCarAvailable(rental.car, rental.start, rental.end) == False:
            raise CarRentalException("Car is not available during that time!")

        self.__repository.store(rental)
        return rental

    def deleteRental(self, rentalId):
        return self._repository.delete(rentalId)

    def isCarAvailable(self, car, start, end):
        """
        Check the availability of the given car to be rented in the provided time period
        car - The availability of this car is verified
        start, end - The time span. The car is available if it is not rented in this time span
        Return True if the car is available, False otherwise
        """
        rentals = self.filterRentals(None, car)
        for rent in rentals:
            if start > rent.end or end < rent.start:
                continue
            return False
        return True

    def filterRentals(self, client, car):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for rental in self.__repository.getAll():
            if client != None and rental.getClient() != client:
                continue
            if car != None and rental.car != car:
                continue
            result.append(rental)
        return result
        
    def mostOftenRentedCarMake(self):
        aux = {}

        for r in self.__repository.getAll():
            if r.car.make not in aux.keys():
                aux[r.car.make] = 1
            else:
                aux[r.car.make] += 1

        for c in self.__carRepo.getAll():
            if c.make not in aux.keys():
                aux[c.make] = 0

        result = []

        for val in aux:
            result.append(CarRentalCount(self.__carRepo.find(val), aux[val]))

        result.sort()

        return result

    def mostOftenRentedCars(self):
        aux = {}

        for r in self.__repository.getAll():
            if r.car.id not in aux.keys():
                aux[r.car.id] = 1
            else:
                aux[r.car.id] += 1

        for c in self.__carRepo.getAll():
            if c.id not in aux.keys():
                aux[c.id] = 0

        result = []

        for val in aux:
            result.append(CarRentalCount(self.__carRepo.find(val),aux[val]))

        result.sort()

        return result

    
    def mostRentedCars(self):
        pass

class MakeRentalCount():
    def __init__(self, make, count):
        self._car = make
        self._count = count

    @property
    def make(self):
        return self._make

    @property
    def count(self):
        return self._count

    def __str__(self):
        return str(self._count) + " ,make: " + str(self._make)

    def __lt__(self, o):
        return self._count < o._count



class CarRentalCount():
    def __init__(self, car, count):
        self._car = car
        self._count = count

    @property
    def car(self):
        return self._car

    @property
    def count(self):
        return self._count

    def __str__(self):
        return str(self._count) + " ,car: " + str(self._car)

    def __lt__(self, o):
        return self._count < o._count

