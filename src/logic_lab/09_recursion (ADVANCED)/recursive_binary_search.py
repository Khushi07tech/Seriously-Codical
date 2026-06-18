# Problem: Search for a target element in a sorted list using recursion
# Algorithm: Recursive Binary Search (Divide and Conquer)
# Approach: Repeatedly divide the search range into halves and discard the irrelevant half
# Key Idea: At each step, compare the target with the middle element and shrink the search space accordingly
# Base Case: If left > right, the element is not present in the list
# Time Complexity: O(log n)
# Space Complexity: O(log n) (due to recursive call stack)


def search(numbers, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == numbers[mid]:
        return mid
    elif target > numbers[mid]:
        return search(numbers, target, mid + 1, right)
    else:
        return search(numbers, target, left, mid - 1)


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 11
    left = 0
    right = len(numbers) - 1

    print(search(numbers, target, left, right))


main()