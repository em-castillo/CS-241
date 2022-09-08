def prompt_number(negative):
    return('Invalid entry. The number must be positive.')


def compute_sum(first, second, third):
    return first + second + third


def main():
    num1 = -1
    num2 = -1
    num3 = -1
    while num1 < 0:
        num1 = int(input('Enter a positive number: '))

        if num1 >= 0:
            print('')
            break

        else:
            print(prompt_number(num1))

    while num2 < 0:
        num2 = int(input('Enter a positive number: '))

        if num2 >= 0:
            print('')
            break

        else:
            print(prompt_number(num2))

    while num3 < 0:
        num3 = int(input('Enter a positive number: '))

        if num3 >= 0:
            print('')
            break

        else:
            print(prompt_number(num3))

    sum = compute_sum(num1, num2, num3)
    print(f'The sum is: {sum}')


# start code with the main function
if __name__ == "__main__":
    main()
