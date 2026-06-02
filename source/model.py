class Product:
    def __init__(self, stock, hold):
        self.hold = hold



    def addhold(self, quantity):
        self.hold += quantity

class Order:
    def add_item(self, product, quantity):
        product.addhold(quantity)
