# Problem: Reverse a list in-place
# Pattern: Two Pointers
# Approach: Use two pointers from start and end, swap elements, move inward
# Key Idea: Modify the original list without extra space
# Time Complexity: O(n)
# Space Complexity: O(1)

nums_list = [1, 2, 3, 4]

left = 0
right = len(nums_list) - 1

while right > left:
    nums_list[left], nums_list[right] = nums_list[right], nums_list[left]

    left += 1
    right -= 1

print(nums_list)