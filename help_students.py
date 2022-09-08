'''Week 06 Data Structure'''
'''
Queue: first in, first out (first come first serve).
- .append() = add or enqueue
- .popleft() = remove or dequeue
Deque: last in, first out
'''
'''Use a queue (i.e., a Python Deque) to keep track of students that are 
requesting help from a TA. When a student asks for help, they are placed 
in the back of the queue. When a TA is available to help, the person at 
the front of the queue is removed from the queue and helped.'''




from collections import deque
class Student:
    def __init__(self):
        self.name = ''
        self.course = ''

    def prompt(self):
        self.name = input('Enter name: ')
        self.course = input('Enter course: ')
        print()

    def display(self):
        print(f'Now helping {self.name} with CS {self.course}')
        print()


class HelpSystem():
    def __init__(self):
        self.waiting_list = deque()
        self.student = Student()

    def is_student_waiting(self):
        '''return True if there are currently students in the waiting_list, and false if not'''
        if len(self.waiting_list) > 0:
            return True
        else:
            return False

    def add_to_waiting(self, student):
        '''receive a Student as a parameter and add them to the waiting list.'''
        self.student.prompt()
        self.waiting_list.append(student)

    def help_next_student(self):
        '''check if there is a student waiting '''
        if self.is_student_waiting() == True:
            # If there is a student waiting then it should remove them from the waiting_list and display,
            print(self.student.display(self.waiting_list))
            self.waiting_list.popleft()

        else:
            # if not, display "No one to help".
            print('No one to help.')
            print()


def main():
    help = HelpSystem()
    selection = 0

    while selection != 3:
        print('Options:')
        print('1. Add a new student')
        print('2. Help next student')
        print('3. Quit')
        selection = int(input('Enter selection: '))
        print()

        if selection == 1:
            help.add_to_waiting()

        elif selection == 2:
            help.help_next_student()

        else:
            print('Goodbye')


if __name__ == "__main__":
    main()
