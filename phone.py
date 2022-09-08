'''W06 Checkpoint Assignment B - Class Inheritance'''


class Phone():
    '''Parent Class - Traditional phone information'''

    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        # asks user to enter each element of a phone number.
        self.area_code = int(input('Area Code: '))
        self.prefix = int(input('Prefix: '))
        self.suffix = int(input('Suffix: '))

    def display(self):
        # displays the phone number
        print(f'({self.area_code}){self.prefix}-{self.suffix}')


class SmartPhone(Phone):
    '''Child Class - Smart phone information and extends the Phone class '''

    def __init__(self):
        # add a member variable
        # super() - calling parent method info
        super().__init__()
        self.email = ''

    def prompt(self):
        # asks user to enter each element of a phone number and email
        # super() - calling parent method info
        super().prompt_number()
        self.email = input('Email: ')

    def display(self):
        # displays the phone number and email
        # super() - calling parent method info
        super().display()
        print(f'{self.email}')


def main():
    # Create Phone object
    phone = Phone()
    print('Phone:')
    phone.prompt_number()
    print()
    print('Phone info:')
    phone.display()
    print()

    # Create SmartPhone Object
    smartphone = SmartPhone()
    print('Smart phone:')
    smartphone.prompt()
    print()
    print('Phone info:')
    smartphone.display()


if __name__ == '__main__':
    main()

# 30 min
