'''Week 09 Checkpoint B - More Exceptions'''


class NegativeNumberError(Exception):
    '''Creates new exception type that inherits from Exception.
    Handles a negative number.'''
    pass


def get_inverse(n):
    '''Accepts a number, n, and then returns the result 1/n.
    Raises an exception according to input'''

    if n == int:
        raise ValueError
    elif n == 0:
        raise ZeroDivisionError
    elif n < 0:
        raise NegativeNumberError
    else:
        return 1/n


def main():
    '''Prompts the user for the value, then pass it to
    get_inverse, and saves the result in a variable.
    Catches each exception and displays an error message.'''
    try:
        num = int(input('Enter a number: '))
        result = get_inverse(num)
        print(f'The result is: {result}')

    except ValueError:
        print('Error: The value must be a number')

    except ZeroDivisionError:
        print('Error: Cannot divide by zero')

    except NegativeNumberError:
        print('Error: The value cannot be negative')


if __name__ == "__main__":
    main()

# checkpoint b: 1 hour
# I did it by myself!
