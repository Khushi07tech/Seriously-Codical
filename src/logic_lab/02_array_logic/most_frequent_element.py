# Problem: Find the most frequent element in a list
# Pattern: Frequency counting + maximum tracking (Hash Map)
# Approach: Build a frequency dictionary, then find the key with highest value
# Time Complexity: O(n)

nums = [1, 2, 2, 3, 1, 4, 2, 1, 1, 1]
freq = {}
max_freq = 0
mode_value = None

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key, value in freq.items():
    if value > max_freq:
        max_freq = value
        mode_value = key

print(f"Mode: {mode_value}")

# Insight:
# This problem combines two core DSA patterns:
# 1. Hashing (frequency map)
# 2. Greedy selection (max tracking)