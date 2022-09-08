'''Week 09 Checkpoint A - Exceptions'''


def main():
    '''Prompts for a number and sends error if is not an integer'''
    valid_input = False

    # while loop so it prompts again if incorrect
    while not valid_input:
        try:
            num = int(input('Enter a number: '))
            valid_input = True

        # handling error if not a integer
        except ValueError:
            print('The value entered is not valid')

    # out of loop because it stops once correct
    print(f'The result is: {num * 2  }')


if __name__ == "__main__":
    main()

# reading: 15 min
# checkpoint a: 30 min
