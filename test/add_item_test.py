import unittest

from source.model import Product, Order, LineItem


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

    def test_AddItemWithQtyOneAddsItemToOrder(self):
        product = Product(stock=7, hold=0, id=327)
        order = Order()

        order.add_item(product, 1)

        self.assertIn(LineItem(product=product, quantity=1), order.items())

if __name__ == '__main__':
    unittest.main()
