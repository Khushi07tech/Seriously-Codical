# Problem: Sort a list using Bubble Sort
# Pattern: Repeated comparison + swapping
# Approach: Multiple passes with adjacent swaps
# Optimization: Stop early if no swaps occur in a full pass
# Key Idea: Largest elements bubble to the end each pass
# Time Complexity: O(n^2)
# Space Complexity: O(1)

numbers = [3, 1, 2, 5, 4]
left = 0
right = left + 1

for n in range(len(numbers) - 1):
    left = 0
    right = 1
    swapped = False

    while right < len(numbers) - n:
        if numbers[left] > numbers[right]:
            swapped = True
            numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right += 1

    if not swapped:
        break

print(numbers)
