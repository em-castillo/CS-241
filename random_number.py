import random  # for testBed Linux
from random import randint  # for code

# testBed random.seed always begin with the same random number
# random.seed(seed_value)

print('Welcome to the number guessing game!')
seed = random.seed(input('Enter random seed: '))
print('')

# min and max random numbers
num = randint(1, 100)

# how many guesses
num_guesses = 0

guess = 0
play_again = True

while play_again == True:

    while guess != num:
        guess = int(input('Please enter a guess: '))
        # adding number to guessing times
        num_guesses = num_guesses + 1

        if (guess > num):
            print('Lower')
            print('')

        elif (guess < num):
            print('Higher')
            print('')

        else:
            print('Congratulations. You guessed it!')
            print(f'It took you {num_guesses} guesses.')
            print('')

    again = input('Would you like to play again (yes/no)? ')

    if (again != 'yes'):
        play_again = False
        print('Thank you. Goodbye.')

    # game starts again, it needs the numbers again.
    num_guesses = 0
    num = randint(1, 100)
    if (again == 'yes'):
        print('')


# do not add comments at the beginning of code because
# it's treated as a header and I cannot submit it.
