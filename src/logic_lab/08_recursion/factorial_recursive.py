# Problem: Calculate the factorial of a number using recursion
# Algorithm: Recursion
# Approach: Multiply the current number by the factorial of the previous number
# Key Idea: Break the problem into smaller factorial calculations until reaching the base case
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursive call stack

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    number = 3
    print(factorial(number))


main()