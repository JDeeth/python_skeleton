import unittest

from source.model import Product, Order


class AddItem(unittest.TestCase):
    def test_AddItemWithSufficientStock(self):
        product = Product(stock=7, hold=0)
        order = Order()

        order.add_item(product, 1)

        self.assertEqual(1, product.hold)

    def test_AddItemWithQtyTwoThenHoldTwo(self):
        product = Product(stock=7, hold=0)
        order = Order()

        order.add_item(product, 2)

        self.assertEqual(2, product.hold)

if __name__ == '__main__':
    unittest.main()
