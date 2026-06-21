# Problem: Sort a list of numbers using Merge Sort
# Algorithm: Divide and Conquer (Recursive Sorting)
# Approach: Split the list into two halves, recursively sort each half, then merge the sorted halves
# Key Idea: Break the problem into smaller subproblems and combine their results in sorted order
# Merge Step: Compare elements from both halves and build a new sorted list using two pointers
# Base Case: A list with 0 or 1 element is already sorted
# Time Complexity: O(n log n)
# Space Complexity: O(n)


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        mid = len(numbers) // 2
        left = merge_sort(numbers[:mid])
        right = merge_sort(numbers[mid:])

        return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def main():
    numbers = [5, 2, 8, 1]
    print(merge_sort(numbers))

main()