class Student:
    # class

    # function that initializes name, lastname, id
    # self references the newly-created object that needs to be initialized.
    def __init__(self):
        self.name = ''
        self.lastname = ''
        self.id = 0


def prompt_student():  # regular function

    # new student object
    student = Student()

    student.name = input('Please enter your first name: ')
    student.lastname = input('Please enter your last name: ')
    student.id = int(input('Please enter your id number: '))

    return student


def display_student(user):  # regular function
    print('')
    print('Your information:')
    print(f'{user.id} - {user.name} {user.lastname}')


def main():
    # call function and asigned it to a variable
    user = prompt_student()
    # Pass the user object to the display_student function to be displayed.
    display_student(user)


# always at first column
if __name__ == "__main__":
    main()

# CLASSES AND OBJECTS
# W03 CHECKPOINT A
# 2 hours and reading
