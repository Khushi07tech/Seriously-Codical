# Problem: Search for a target element in a sorted list
# Algorithm: Binary Search
# Approach: Repeatedly divide the search space in half
# Key Idea: Compare middle element and eliminate half the array each time
# Time Complexity: O(log n)
# Space Complexity: O(1)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3

left = 0
right = len(numbers) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if target == numbers[mid]:
        print(f"Found at index {mid}")
        found = True
        break
    elif target > numbers[mid]:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print("Not Found")