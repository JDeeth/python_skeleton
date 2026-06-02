import unittest

class Product:
    def __init__(self, stock, hold):
        pass

    def hold(self):
        return 1

class Order:
    def add_item(self, product, quantity):
        pass

class AddItem(unittest.TestCase):
    def test_AddItemWithSufficientStock(self):
        product = Product(stock=7, hold=0)
        order = Order()
        order.add_item(product, 1)
        self.assertEqual(1, product.hold())


if __name__ == '__main__':
    unittest.main()
