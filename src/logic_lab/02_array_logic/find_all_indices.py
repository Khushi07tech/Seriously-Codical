# Problem: Find all indices of a target element in a list
# Pattern: Linear traversal + result accumulation
# Approach: Traverse list, track index, and store matches in a list
# Key Idea: Do not stop at first match; collect all occurrences
# Time Complexity: O(n)
# Space Complexity: O(k)  # k = number of matches

nums = [1, 2, 4, 2, 8, 2]
target = 2
current_index = 0
indices = []

for num in nums:
    if num == target:
        indices.append(current_index)
    current_index += 1

print(f"{target} found at indexes {indices}")