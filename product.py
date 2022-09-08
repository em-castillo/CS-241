'''W04 Prove'''
'''This file gets the total price and quatity of a product.'''


class Product:
    # Initializes id, name, price, quatity
    def __init__(self, id='', name='', price=0, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    # Returns the price multiplied by the quantity
    def get_total_price(self):
        total = self.price * self.quantity
        return total  # always assigned variable to return

    # Displays the products name, quantity, and total price
    def display(self):
        print(f'{self.name} ({self.quantity}) - ${self.get_total_price():.2f}')
    # .format accepts strings
