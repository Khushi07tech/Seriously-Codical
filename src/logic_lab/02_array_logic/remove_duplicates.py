# Problem: Remove duplicates from a list while preserving order
# Pattern: Filtering + seen-check
# Approach: Traverse list and add element only if not already present
# Key Idea: Use a secondary list to track unique elements
# Time Complexity: O(n^2)  # due to 'not in' check
# Space Complexity: O(n)

nums = [1, 2, 4, 2, 8, 2]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)