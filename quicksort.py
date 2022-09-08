'''Week 10 Team Activity - Strech Challenge'''
''' q   uicj sort compares left side to right side.'''
"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the quick sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def quicksort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """

    quickSortHelper(items, 0, len(items)-1)


def quickSortHelper(items, first, last):
    if first < last:

        splitpoint = partition(items, first, last)

        quickSortHelper(items, first, splitpoint-1)
        quickSortHelper(items, splitpoint+1, last)


def partition(items, first, last):
    pivotvalue = items[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and items[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while items[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = items[leftmark]
            items[leftmark] = items[rightmark]
            items[rightmark] = temp

    temp = items[first]
    items[first] = items[rightmark]
    items[rightmark] = temp

    return rightmark


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    quicksort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
