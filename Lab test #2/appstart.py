from repository.driverRepository import DriverRepository
from repository.orderRepository import OrderRepository
from controller.driverController import DriverController
from controller.orderController import OrderController

from ui.menu import UI

def start():
    repoD = DriverRepository()
    repoO = OrderRepository()

    controllerD = DriverController(repoD)
    controllerO = OrderController(repoO)

    ui = UI(controllerD, controllerO)

    ui.mainMenu()

start()