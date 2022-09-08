'''Week 08 Checkpoint A - Getters and Setters'''


class GPA:
    '''Creates a class to hold a student's GPA'''

    def __init__(self):
        '''Creates an __init__() function to set the initial value to 0.0.'''
        self.gpa = 0.0

    def get_gpa(self):
        '''GPA getter method'''
        return self.gpa

    def set_gpa(self, value):
        '''GPA setter method'''
        if value < 0:
            self.gpa = 0
        elif value > 4:
            self.gpa = 4.0
        else:
            # keeps value(input)
            self.gpa = value

    def get_letter(self):
        '''Determines the correct letter for the stored gpa, and returns it.'''
        if self.gpa >= 0.0 and self.gpa <= 0.99:
            return 'F'
        elif self.gpa >= 1.0 and self.gpa <= 1.99:
            return 'D'
        elif self.gpa >= 2.0 and self.gpa <= 2.99:
            return 'C'
        elif self.gpa >= 3.0 and self.gpa <= 3.99:
            return 'B'
        elif self.gpa == 4.0:
            return 'A'

    def set_letter(self, letter):
        '''Determines the appropriate gpa value and stores that.'''
        # does not return it
        if letter == 'F':
            self.gpa = 0.0

        elif letter == 'D':
            self.gpa = 1.0

        elif letter == 'C':
            self.gpa = 2.0

        elif letter == 'B':
            self.gpa = 3.0

        elif letter == 'A':
            self.gpa = 4.0


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()

# reading = 15min
# checkpoint = 1 hour 30 min
