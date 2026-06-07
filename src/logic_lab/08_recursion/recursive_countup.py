# Problem: Print numbers in ascending order using recursion
# Algorithm: Recursion
# Approach: Recursively reach the base case first, then print numbers while returning
# Key Idea: Work is performed after the recursive call, causing values to print in ascending order
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursive call stack

def countup(number):
    if number == 0:
        return
    else:
        countup(number-1)
        print(number)


def main():
    number = 5
    countup(number)


main()