''' W04 Checkpoint B - '''
''' breaking up one file into three. One class or function in each file'''


'''Import Address class'''
# from address (file name without .py) import Address (class) to use its info


'''Credit Card class contains card info'''




from file_address import Address
class CreditCard:
    """ Contains a credit card that has two addressess"""

    def __init__(self):
        self.name = ""
        self.number = ""
        self.mailing_address = Address()  # getting info from Address class
        self.billing_address = Address()

    # displays card info and address from Address class
    def display(self):
        print(self.name)
        print(self.number)

        print("Mailing Address:")
        self.mailing_address.display()

        print("Billing Address:")
        self.billing_address.display()
