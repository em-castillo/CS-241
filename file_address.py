''' W04 Checkpoint B - '''
''' breaking up one file into three. One class or function in each file'''


''' Address class that contains user's info and diplays it'''


class Address:
    """ Contains a street address """

    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    # displays user's info
    def display(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))
