'''Week 08 Checkpoint B - Getters and Setters'''


class GPA:
    '''Creates a class to hold a student's GPA'''

    def __init__(self):
        '''Creates an __init__() function to set the initial value to 0.0.'''
        # underscore added to variable
        self._gpa = 0.0

    # add underscore to functions
    def _get_gpa(self):
        '''GPA getter method'''
        return self._gpa

    def _set_gpa(self, value):
        '''GPA setter method'''
        if value < 0:
            self._gpa = 0
        elif value > 4:
            self._gpa = 4.0
        else:
            # keeps value(input)
            self._gpa = value

    # add property named gpa to functions -> property object
    gpa = property(_get_gpa, _set_gpa)

    # specify property on both functions (need same function name to work = 'letter')
    @property
    def letter(self):
        '''Determines the correct letter for the stored gpa, and returns it.'''
        if self._gpa >= 0.0 and self._gpa <= 0.99:
            return 'F'
        elif self._gpa >= 1.0 and self._gpa <= 1.99:
            return 'D'
        elif self._gpa >= 2.0 and self._gpa <= 2.99:
            return 'C'
        elif self._gpa >= 3.0 and self._gpa <= 3.99:
            return 'B'
        elif self._gpa == 4.0:
            return 'A'

    @letter.setter
    def letter(self, letter):
        '''Determines the appropriate gpa value and stores that.'''
        # does not return it
        if letter == 'F':
            self._gpa = 0.0

        elif letter == 'D':
            self._gpa = 1.0

        elif letter == 'C':
            self._gpa = 2.0

        elif letter == 'B':
            self._gpa = 3.0

        elif letter == 'A':
            self._gpa = 4.0

    # add property named letter
    # letter = property(?) -> no property object...
    # when property decorator is used


def main():
    student = GPA()

    # change get_gpa to only gpa, same with letter

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))


if __name__ == "__main__":
    main()


# checkpoint b = 1 hour
