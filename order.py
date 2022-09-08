'''W04 Prove'''
'''This file calculates subtotal, tax, total, add products, and display receipt.'''


class Order:
    # Initializes id, products
    def __init__(self):
        self.id = ''
        self.products = []  # create empty list

    # Sums the price of each product and returns it
    def get_subtotal(self):
        price_sum = 0
        for product in self.products:
            price_sum += product.get_total_price()

        return price_sum

    # Returns 6.5% times the subtotal
    def get_tax(self):
        tax = self.get_subtotal() * 0.065
        return tax

    # Returns the subtotal plus the tax
    def get_total(self):
        total = self.get_subtotal() + self.get_tax()
        return total

    # Adds the provided product to the list / add = append list
    def add_product(self, product):
        self.products.append(product)

    # Displays a receipt in the format:
    def display_receipt(self):
        print(f'Order: {self.id}')
        # list of products
        for product in self.products:
            product.display()  # p1.display -> p2.display
        print(f'Subtotal: ${self.get_subtotal():.2f}')
        print(f'Tax: ${self.get_tax():.2f}')
        print(f'Total: ${self.get_total():.2f}')
