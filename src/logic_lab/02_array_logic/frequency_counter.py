nums = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)