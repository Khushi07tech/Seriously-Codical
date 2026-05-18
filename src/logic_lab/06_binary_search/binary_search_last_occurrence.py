# Problem: Find the last occurrence of a target in a sorted list (with duplicates)
# Algorithm: Binary Search (Modified)
# Approach: Use binary search and continue searching right even after finding target
# Key Idea: Store potential answer and shrink search space to the right half
# Time Complexity: O(log n)
# Space Complexity: O(1)

numbers = [1, 2, 3, 3, 3, 4, 4, 5]
target = 4

# Search boundaries
left = 0
right = len(numbers) - 1

# Store result index (default: not found)
answer = -1

while left <= right:

    mid = (left + right) // 2

    # If target found, store index and search right side for last occurrence
    if target == numbers[mid]:
        answer = mid
        left = mid + 1

    # If target is greater, ignore left half
    elif target > numbers[mid]:
        left = mid + 1

    # If target is smaller, ignore right half
    else:
        right = mid - 1


print(answer)