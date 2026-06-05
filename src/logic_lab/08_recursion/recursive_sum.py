# Problem: Calculate the sum of all elements in a list using recursion
# Algorithm: Recursion
# Approach: Add the first element to the recursive sum of the remaining list
# Key Idea: Break the list into first element + rest of the list until empty
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursive call stack

def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def main():
    numbers = [1, 2, 3, 4]
    print(recursive_sum(numbers))

main()