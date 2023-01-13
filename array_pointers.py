#!/usr/bin/env python3


def find_pair_that_sum(sorted_array, target):
    """
    Given an array of sorted numbers and a target sum,
    find a pair in the array whose sum is equal to the given target.
    """
    left = 0
    right = len(sorted_array) - 1

    while left <= right:
        current_sum = sorted_array[left] + sorted_array[right]
        if current_sum == target:
            return (sorted_array[left], sorted_array[right])
        elif current_sum < target:
            left += 1 # We need to try with a larger number
        else:
            right -= 1 # Look for a smaller number to approach the target
    return (None, None)


if __name__ == "__main__":
    array = [ 1, 32, 64, 122, 877, 1009]
    print(f"Given {array}")
    for target in [154, 20]:
        print(f"Find 2 numbers that sum {target}: {find_pair_that_sum(array, target)}")
