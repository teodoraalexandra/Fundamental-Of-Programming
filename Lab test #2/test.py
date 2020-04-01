from repository.orderRepository import OrderRepository
from controller.orderController import OrderController
from domain.order import Order

import unittest
class Test_(unittest.TestCase):
    def setUp(self):
        self.repo = OrderRepository("orders.txt")
        self._controller = OrderController(self.repo)

    def test_add(self):
        o1 = Order(1, 10)
        o2 = Order(2, 20)
        o3 = Order(3, 30)
        init = len(self._controller.getAll())

        self._controller.addOrder(o1)
        self.assertEqual(len(self._controller.getAll()), init+1)
        self._controller.addOrder(o2)
        self.assertEqual(len(self._controller.getAll()), init + 2)
        self._controller.addOrder(o3)
        self.assertEqual(len(self._controller.getAll()), init + 3)



