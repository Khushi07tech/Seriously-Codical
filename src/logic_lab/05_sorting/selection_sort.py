# Problem: Sort a list using Selection Sort
# Pattern: Find minimum and place it correctly
# Approach: For each position, find the smallest element in the remaining list
# Key Idea: Only one swap per pass
# Time Complexity: O(n^2)
# Space Complexity: O(1)

numbers = [3, 2, 5, 4, 1]

for i in range(len(numbers) - 1):
    smallest_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest_index]:
            smallest_index = j
    numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

print(numbers)