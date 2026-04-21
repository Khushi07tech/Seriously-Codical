nums = [20, 20, 50, 50, 1, 2]

largest_num = float('-inf')
sec_largest_num = float('-inf')

for num in nums:
    # Use >= to ensure duplicates push the previous largest into the second slot
    if num >= largest_num:
        sec_largest_num = largest_num
        largest_num = num
    elif largest_num > num > sec_largest_num:
    # This only runs if the number wasn't the new largest
        sec_largest_num = num

print(f"Second largest number is {sec_largest_num}")

