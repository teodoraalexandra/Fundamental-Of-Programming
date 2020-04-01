from repository.driverRepository import DriverRepository
from repository.orderRepository import OrderRepository
from controller.driverController import DriverController
from controller.orderController import OrderController
from domain.order import Order
from domain.driver import Driver


class UI:
    def __init__(self, controllerD, controllerO):
        self._controllerD = controllerD
        self._controllerO = controllerO

    def mainMenu(self):
        ok = True
        while ok:
            try:
                UI.printMenu(self)
                command = input("Enter command: ")
                if command == '0':
                    print("Bye bye")
                    ok = False

                elif command == "1":
                    o = UI.readOrder(self)
                    self._controllerO.addOrder(o)

                elif command == '2':
                    for o in self._controllerO.getAll():
                        print(str(o))

                elif command == '3':
                    id = int(input("Enter the id of the driver: "))
                    for i in self._controllerD.getAll():
                        if i.getDriverId() == id:
                            name = i.getName()

                    totalkm = 0
                    for i in self._controllerO.getAll():
                        if i.getDriverId() == id:
                            totalkm += i.getDistance()
                    income = 2.5 * totalkm

                    print("DRIVER:")
                    print("Id:", id)
                    print("Name:", name)
                    print("Income:", income)

                else:
                    raise ValueError("Invalid command. Enter 1, 2, 3 or 0")

            except Exception as me:
                print(me)

    def readOrder(self):
        while True:
            try:
                driverId = int(input("Enter driver ID= "))
                distance = int(input("Enter distance in km= "))
                if distance > 1 and self._controllerD.checkId(driverId):
                    return Order(driverId, distance)
                else:
                    print("Unavaible driver Id or distance is less than 1 km")
            except ValueError:
                print("Something went wrong")
        return []


    def printMenu(self):
        menu = "\nCommands:\n"
        menu += "\t1. Add an order \n"
        menu += "\t2. Display all orders\n"
        menu += "\t3. Compute an income\n"
        menu += "\t0. Exit\n"
        print(menu)
