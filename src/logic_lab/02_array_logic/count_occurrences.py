# Problem: Count how many times a target element appears in a list
# Pattern: Linear traversal + counting (accumulation)
# Approach: Iterate through the list and increment counter when match is found
# Key Idea: Must check every element (no early exit like search)
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [3, 8, 6, 5, 3, 3]
target = int(input("Target: "))
t_count = 0

def find_target(t_count):
    for num in nums:
        if num == target:
            t_count += 1
    return t_count

result = find_target(t_count)

if result:
    print(f"{target} found {result}x")
else:
    print("Not Found")
