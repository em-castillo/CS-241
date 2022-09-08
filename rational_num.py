from math import gcd
# gcd greatest common denominator


class Rational:

    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def prompt(self):
        self.numerator = int(input('Enter the numerator: '))
        self.denominator = int(input('Enter the denominator: '))

    def display(self):
        wholeNumber = int(self.numerator/self.denominator)
        # self.numerator % self.denominator
        newNumerator = int(self.numerator - wholeNumber * self.denominator)
        newDenominator = int(self.denominator)

        if self.numerator > self.denominator:
            print("{} {}/{}".format(wholeNumber, newNumerator, newDenominator))
        else:
            print("{}/{}".format(self.numerator, self.denominator))

    def display_decimal(self):  # does the math
        result = float(self.numerator / self.denominator)
        print(result)

    def reduce(self):
        factor = gcd(self.numerator, self.denominator)
        new_numerator = int(self.numerator / factor)
        new_denominator = int(self.denominator / factor)
        print(f'{new_numerator}/{new_denominator}')

    def multiply_by(self):
        mult_numerator = int(input('Enter a number: '))
        print("{}/{}".format(self.numerator * mult_numerator, self.denominator))

    # member functions or methods


def main():
    # new object
    rat = Rational()
    # methods
    rat.display()
    rat.prompt()
    rat.display()
    rat.display_decimal()
    rat.reduce()
    rat.multiply_by()


if __name__ == "__main__":
    main()


# W03 TEAM ACTIVITY
 # 1 hour
