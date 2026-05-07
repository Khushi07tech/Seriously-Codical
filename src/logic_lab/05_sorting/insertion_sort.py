# Problem: Sort a list using Insertion Sort
# Pattern: Build a sorted portion step-by-step
# Approach: Take one element and insert it into its correct position
# Key Idea: Shift larger elements to the right, then insert current value
# Time Complexity:
#   Best Case: O(n)
# Space Complexity: O(1)

numbers = [3, 1, 2, 5, 4]

for i in range(len(numbers)):
    j = i - 1

    current_value = numbers[i]

    while j>= 0 and numbers[j] > current_value:

        #Shift to right
        numbers[j+1] = numbers[j]
        j -= 1

    #Insert current value at j+1
    numbers[j+1] = current_value


print(numbers)
