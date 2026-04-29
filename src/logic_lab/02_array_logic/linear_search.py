# Problem: Check if a target element exists in a list
# Algorithm: Linear Search
# Approach: Traverse the list and compare each element with the target
# Key Idea: Stop early if target is found
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [3, 8, 6, 5]
target = int(input("Target: "))

def find_target():
    for num in nums:
        if num == target:
            return True
    return False

result = find_target()
if result:
    print("Found")
else:
    print("Not Found")