'''W04 Prove'''
'''
This file counts oders, gets total price, adds orders to the list,
displays summary and receipt
'''


class Customer:
    # Initializes id, name, orders
    def __init__(self):
        self.id = ''
        self.name = ''
        self.orders = []

    # Returns the number of orders
    def get_order_count(self):
        count = len(self.orders)
        return count  # assigned a variable to return

    # Returns the total price of all orders combined
    def get_total(self):
        total = 0
        for order in self.orders:
            total += order.get_total()
        return total

    # Adds the provided order to the list of orders
    def add_order(self, order):
        self.orders.append(order)

    # Displays a summary
    def display_summary(self):
        print(f"Summary for customer '{self.id}':")
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: ${self.get_total():.2f}')

    # Displays all the orders' receipts
    def display_receipts(self):
        print(f"Detailed receipts for customer '{self.id}':")
        print(f'Name: {self.name}')
        # print()
        for order in self.orders:
            print()
            order.display_receipt()
