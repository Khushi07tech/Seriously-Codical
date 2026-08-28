def subsets(numbers, index, current_subset):
    if index == len(numbers):
        return
    else:
        current_subset.append(numbers[index])


def main():
    numbers = [1, 2]
    index = 0
    current_subset = []
    subsets(numbers, index, current_subset)

