# Problem: Find the index of the first occurrence of a target in a list
# Algorithm: Linear Search
# Approach: Traverse list while tracking index manually
# Key Idea: Stop as soon as target is found
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [1, 2, 4, 8]
target = int(input("Target: "))
current_index = 0

for num in nums:
    if num == target:
        print(f"{target} found at index {current_index}")
        break
    current_index += 1