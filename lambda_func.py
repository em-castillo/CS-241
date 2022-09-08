'''Week 12 Data Structure - Lambda Functions'''
''' Lambda:
lambda argument_list: expression
sum = lambda x, y : x + y
sum(3,4)'''
'''Map:
r = map(function_name, sequence(list))'''
'''Filter:
filter(function, sequence)'''
'''Reduce:
reduce(func, seq)'''

"""
Purpose: This file is a starting point to help you practice using lambda functions.
"""




import functools
def get_part1_list():
    """
    Filters a list to return even numbers greater than 33.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here that uses filter and a lambda function to filter
    # the list so that it only contains even numbers greater than 33.
    new_numbers = []
    even_num = list(filter(lambda x: x % 2 == 0 and x > 33, new_numbers)
                    )

    return new_numbers


def get_part2_list():
    """
    Maps a lambda function to a list to square each number and add one.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here than uses map and a lambda function to go through
    # each number in the list, square it and then add one to the result
    new_numbers = []
    square_num = list(map(lambda x: x**2 and x + 1, new_numbers))

    return new_numbers


def get_part3_list():
    """
    Reduces a list to its product
    """
    numbers = [x for x in range(1, 100)]

    # TODO: Write a line here that uses reduce and a lambda function to
    # multiply all the numbers in the list together and return the product
    product = 0
    # functools.reduce(lambda )
    return product


def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()
