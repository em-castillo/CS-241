class Complex:

    def __init__(self):
        self.real = 0
        self.imaginary = 0

    # prompt and display use self as a parameter because they are member functions

    def prompt(self):  # member function is inside class

        self.real = int(input('Please enter the real part: '))
        self.imaginary = int(input('Please enter the imaginary part: '))

        # return self / don't need to return because is a member function

    def display(self):  # self added so it recognizes real and imaginary values
        print(f'{self.real} + {self.imaginary}i')


# Given code


def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    # 2 complex numbers created
    c1 = Complex()  # real
    c2 = Complex()  # imaginary

    # display them
    print("The values are:")
    c1.display()
    c2.display()

    # prompt user for each one
    print()
    c1.prompt()

    print()
    c2.prompt()

    # display them again
    print("\nThe values are:")
    c1.display()
    c2.display()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()

# W03 CHECKPOINT B
