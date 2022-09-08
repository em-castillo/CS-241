odd = []  # or odd = list()
even = []

num = int(input('Enter a number (0 to quit): '))

while num != 0:
    if num % 2 == 0:
        even.append(num)  # or odd.insert(num)
        num = int(input('Enter a number (0 to quit): '))
        # input inside each statement so it appends first num and not last number (0)

    else:
        odd.append(num)
        num = int(input('Enter a number (0 to quit): '))

print()
print('Even numbers:')
for even_num in even:
    print(even_num)

print()
print('Odd number:')
for odd_num in odd:
    print(odd_num)

# W03 DATA STRUCTURE HOMEWORK

# O(1) Data access by index - You can jump right to the spot you want, based on its index.

# O(n) Insertion to the beginning of the list - Everything in the list most be shuffled down to make room for the new item.

# O(n) Removal from the beginning of the list - Everything must be shuffled up to fill the empty spot.

# O(1) (amortized) Insertion at the end of the list - See discussion above.

# O(1) Remove at the end of the list - Nothing needs to be shuffled.
