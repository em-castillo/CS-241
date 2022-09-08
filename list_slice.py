'''Week 10 - Data Structure List Manipulation'''

# list
numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

'''Insert number 5 at beginning'''
# 0 is the index, 5 item to be inserted
numbers.insert(0, 5)
print(f'Insert: {numbers}')

'''Remove the number 2348 based on its value'''
# pop is with index
# clear removes the whole list.
numbers.remove(2348)
print(f'Remove: {numbers}')

'''Create a second list of 5 different numbers and add them to the end of the list'''
more_numbers = [1, 2, 3, 4, 5]
numbers.extend(more_numbers)
print(f'Extend: {numbers}')

'''Sort the list using the built in sorting algorithm.'''
numbers.sort()
print(f'Sort: {numbers}')

'''Sort the list backwards'''
numbers.reverse()
print(f'Sort backwards: {numbers}')

'''Count the number of 12's in the list.'''
print(f"Number of 12's present: {numbers.count(12)}")

'''Find the index of the number 96.'''
print(f'Find index: {numbers.index(96)}')

'''Use slicing to get the first half of the list, then get the second half of the list'''
# print total indexes on list to slice later
print(f'Index lenght: {len(numbers)}')
# 1 half
print(f'1 half of list: {numbers[0:10]}')
# 2 half
# no number after : to include last number
print(f'2 half of list: {numbers[10:]}')

'''Use slicing to create a new list that has every other item from the original list'''
numbers_one = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
# no numbers between : to include the whole list
# stride. 2 means it skips every other number. 1 is the default, reades each item.
print(f'Print every other number on list: {numbers_one[::2]}')

'''Use slicing to get the last 5 items of the list.'''
print(f'Print 5 last number of list: {numbers_one[-5:]}')

# Data: 1 hour
