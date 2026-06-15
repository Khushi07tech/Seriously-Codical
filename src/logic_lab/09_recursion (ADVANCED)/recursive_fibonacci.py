# Problem: Find the nth Fibonacci number using recursion
# Algorithm: Recursion
# Approach: Compute the current Fibonacci number as the sum of the two previous Fibonacci numbers
# Key Idea: Break the problem into two smaller Fibonacci calculations until reaching base cases
# Base Case: fib(0) = 0 and fib(1) = 1
# Time Complexity: O(2^n)
# Space Complexity: O(n)


def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number-1) + fib(number-2)


def main():
    number = 6
    print(fib(number))


main()