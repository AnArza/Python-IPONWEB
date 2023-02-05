class Product:
    def __init__(self, price, id, quantity):
        if type(price) != int or price < 0 or type(id) != int or id < 0 or type(quantity) != int or quantity < 0:
            raise ProductError
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return f"Price {self.price}\nID {self.id}\nQuantity {self.quantity}"

    def buy(self, count):
        if count > self.quantity:
            raise ProductError("Not that much product")
        self.quantity -= count


class Inventory:
    def __init__(self, list_of_prods):
        for p in list_of_prods:
            if type(p) != Product:
                raise InventoryError("All members of the list should be products")
        self.list_of_prods = list_of_prods

    def __repr__(self):
        res = ''
        for p in self.list_of_prods:
            res += f"Price {p.price}\nID {p.id}\nQuantity {p.quantity}" + '\n'
        return res

    def get_by_id(self, id):
        for p in self.list_of_prods:
            if p.id == id:
                return p
        raise InventoryError("No product with such id")

    def sum_of_products(self):
        res = 0
        for p in self.list_of_prods:
            res += p.price * p.quantity
        return res


class ProductError(Exception):
    def __init__(self, message="Invalid product"):
        super().__init__(message)


class InventoryError(Exception):
    pass


p1 = Product(1500, 1, 2)
p2 = Product(250, 2, 5)
p3 = Product(800, 3, 45)
p1.buy(2)
inv = Inventory([p1, p2, p3])
print(inv)
print(inv.get_by_id(2))
print(inv.sum_of_products())
