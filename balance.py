'''W05 Prove - Data Structure'''
from collections import deque


def Balance():
    stack = deque()
    braces = {'{': '}', '(': ')', '[': ']'}
    check_balance = True

    # Open the file
    file = input('File: ')
    read_file = open(file, 'r')
    # Read through it character by character
    # One way to do this for this program, is to read line by line
    # and then call line.strip() to get rid of any whitespace
    for line in read_file:
        line = line.split()

        # If current character is any type of opening brace: (, {, [
        # push it (the current character) on to a stack
        for character in line:
            if character == '(' or character == '{' or character == '[':
                stack.append(character)

        # if current character is any type of closing brace: ), }, ]
            # compare it to the thing on the top of the stack
            # If the stack is empty (nothing to compare)
            # Quit now, it doesn't match
            # if they match (meaning closing of the same type):
            # We're good
            # Pop the opening brace off the stack
            # If they don't match
            # Quit now, and tell them the braces don't match
            # # after reading the complete file
            else:
                if stack:
                    top = stack.pop()
                    if braces[top] != character:
                        check_balance = False

                else:
                    check_balance = False

    if check_balance == False:
        print('Not balanced')

    elif check_balance == True:
        print('Balanced')

    read_file.close()

    # If there is anything on the stack, the braces didn't match


def main():
    Balance()


if __name__ == '__main__':
    main()


# 1 test fail of 6.
# first file was only one brace --> [
# it printed balaced instead of not balanced
