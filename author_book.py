'''W04  Checkpoint A'''

'''Create a class to model books and the author that wrote it'''

'''Create a class for a Person that contains a name and a birth year. '''
'''The author of a book will be a Person object.'''


class Person:
    # initialize Person
    def __init__(self):
        self.name = 'anonymous'
        self.birth_year = 'unknown'

    # displays person's info
    def display(self):
        # return str(self.name) + ' (b. ' + (self.birth_year) + ')'
        print(f'{self.name} (b. {self.birth_year})')


'''Create a class for a Book that contains a title, an author (of type Person),'''
''' and a publisher.'''


class Book:
    # initialize Book
    def __init__(self):
        self.title = 'untitled'
        self.author = Person()  # author instance of Person
        self.publisher = 'unpublished'

    def prompt(self):
        print('Please enter the following:')
        # name belongs to author instance
        self.author.name = input('Name: ')
        # birth_year belongs to author instance
        self.author.birth_year = input('Year: ')
        self.title = input('Title: ')
        self.publisher = input('Publisher: ')
        print()

    # displays book info

    def display(self):
        print(self.title)
        print('Publisher:')
        print(self.publisher)
        print('Author:')
        self.author.display()


def main():
    new_book = Book()
    new_book.display()
    print()
    new_book.prompt()
    new_book.display()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()


# 4 hours

# instance = Class()
# Call instances. I work with instances.
