'''W06 Checkpoint Assignment A - Class Inheritance'''


class Book:
    '''Parent Class - normal book info'''

    def __init__(self):
        # initializes variables
        self.title = ''
        self.author = ''
        self.publication_year = 0

    def prompt_book_info(self):
        # prompts user for info
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = int(input('Publication Year: '))

    def display_book_info(self):
        # shows input in a specific format
        print(f'{self.title} ({self.publication_year}) by {self.author}')


class Texbook(Book):
    '''Child class - text book info'''

    def __init__(self):
        # adds a member variable
        # super() - calling the rest of parent method
        super().__init__()
        self.subject = ''

    def prompt_subject(self):
        # prompts subject of the book
        self.subject = input('Subject: ')

    def display_subject(self):
        # displays subject of the book
        print(f'Subject: {self.subject}')


class Picturebook(Book):
    '''Child class - picture book info'''

    def __init__(self):
        # adds another member variable
        super().__init__()
        self.illustrator = ''

    def prompt_illustrator(self):
        # prompts for illustrator
        self.illustrator = input('Illustrator: ')

    def display_illutstrator(self):
        # displays illustrator
        print(f'Illustrated by {self.illustrator}')


def main():
    # Book object
    book = Book()
    book.prompt_book_info()
    print()
    book.display_book_info()
    print()

    # Textbook object
    textbook = Texbook()
    textbook.prompt_book_info()
    textbook.prompt_subject()
    print()
    textbook.display_book_info()
    textbook.display_subject()
    print()

    # Picturebook object
    picturebook = Picturebook()
    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    print()
    picturebook.display_book_info()
    picturebook.display_illutstrator()


if __name__ == '__main__':
    main()

# 35 min
