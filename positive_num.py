def prompt_number():
    num = -1

    while num < 0:
        num = int(input('Enter a positive number: '))

        if num >= 0:
            print('')
            # return number so compute() has positive numbers to sum
            return num

        else:
            print('Invalid entry. The number must be positive.')


def compute_sum(first, second, third):
    return first + second + third


def main():
    # It needs 3 positive numbers
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()

    sum = compute_sum(num1, num2, num3)
    print(f'The sum is: {sum}')


# start code with the main function
if __name__ == "__main__":
    main()
