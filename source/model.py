class Product:
    def __init__(self, stock, hold):
        self._hold = hold

    def hold(self):
        return self._hold

    def addhold(self, quantity):
        self._hold += quantity

class Order:
    def add_item(self, product, quantity):
        product.addhold(quantity)
