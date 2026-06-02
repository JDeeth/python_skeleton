class Product:
    def __init__(self, stock, hold, id=0):
        self.hold = hold
        self.id = id

    def add_hold(self, quantity):
        self.hold += quantity

    def __eq__(self, other):
        return isinstance(other, Product) and other.id == self.id


class Order:
    _items = []

    def add_item(self, product, quantity):
        product.add_hold(quantity)
        self._items.append(Item(product, quantity))

    def items(self):
        return self._items


class Item:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __eq__(self, other):
        return isinstance(other, Item) and other.product == self.product and other.quantity == self.quantity
