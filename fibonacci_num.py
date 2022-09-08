'''Week 07 Data Structure - Recursion'''
'''
Recursion: a function calls itself
ex: 
function HelloWorld(count) {
  if (count < 1) returnprint("Hello World!") HelloWorld(count - 1) # count - 1 -> repeats 1 time
}
base case: when function stop calling itself and returns (usually 0 or 1)
'''


def fib(n):
    '''Write a program that uses recursion to compute 
    the n-th item in the Fibonacci sequence.'''
    # base case
    if (n <= 0):
        return 0
    # base case
    elif (n == 1):
        return 1
    # compute fibonacci number
    return fib(n - 2) + fib(n - 1)


def main():
    '''Write a main function that asks the user for the index 
    of the Fibonacci number they want to compute. It should 
    then pass this to your fib function, and display the result.'''

    n = int(input('Enter a Fibonacci index: '))

    print(f'The Fibonacci number is: {fib(n)}')


if __name__ == "__main__":
    main()

# 1 hour
