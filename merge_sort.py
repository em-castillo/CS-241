'''Week 10 Team Activity'''
'''Merge divides list in two every time like a tree.'''
"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    # SPLIT LIST
    # Base case: if the list has more than one item in the list execute code
    if len(items) > 1:
        # NOTE: The double forward slash in Python is known as the integer division operator.
        # It will divide the left by the right, and only keep the whole number component
        # one / -> retuns float, two // -> returns integer
        # Break the list into halves
        half = len(items) // 2
        left_half = items[:half]
        right_half = items[half:]

        # Recursively call this function to sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # MERGING LIST
        left_iteration = 0  # left half
        right_iteration = 0  # right half
        complete_iteration = 0  # complete list

        # As long as there are more items in each list
        while left_iteration < len(left_half) and right_iteration < len(right_half):
            # Get the smaller item from whichever part its in
            if left_half[left_iteration] <= right_half[right_iteration]:
                items[complete_iteration] = left_half[left_iteration]
                left_iteration += 1

            else:
                items[complete_iteration] = right_half[right_iteration]
                right_iteration += 1

            complete_iteration += 1

        # At this point, one or the other size is done

        # Copy any remaining items from half 1
        while left_iteration < len(left_half):
            items[complete_iteration] = left_half[left_iteration]
            left_iteration += 1
            complete_iteration += 1

        # Copy any remaining items from half 2
        while right_iteration < len(right_half):
            items[complete_iteration] = right_half[right_iteration]
            right_iteration += 1
            complete_iteration += 1

        return items


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
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
