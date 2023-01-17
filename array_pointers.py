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
            left += 1  # We need to try with a larger number
        else:
            right -= 1  # Look for a smaller number to approach the target
    return (None, None)


def remove_duplicates(sorted_array):
    """
    Given an array of sorted numbers, remove all duplicate number instances
    from it in-place, such that each element appears only once.
    Move all the unique elements at the beginning of the array
    and after moving return the length of the subarray that has no duplicate in it.
    """
    next_new_index = 1
    index = 0

    while index < len(sorted_array):
        if sorted_array[index] != sorted_array[next_new_index - 1]:
            sorted_array[next_new_index] = sorted_array[index]
            next_new_index += 1
        index += 1

    return next_new_index


def remove_key(array, key):
    """
    Given an unsorted array of numbers and a target ‘key’, remove all
    instances of ‘key’ in-place and return the new length of the array
    """
    index = 0
    copy_at = 0

    while index < len(array):
        if array[index] != key:
            array[copy_at] = array[index]
            copy_at += 1
        
        index += 1

    return copy_at

if __name__ == "__main__":
    # array = [ 1, 32, 64, 122, 877, 1009]
    # print(f"Given {array}")
    # for target in [154, 20]:
    #     print(f"Find 2 numbers that sum {target}: {find_pair_that_sum(array, target)}")

    # print("Remove dups")
    # data = (([2, 3, 3, 3, 6, 9, 9], 4), ([2, 2, 2, 11], 2))

    # for array, expected_length in data:
    #     print(array)
    #     assert remove_duplicates(array) == expected_length
    #     print(array)

    # print("Remove key")
    # data = (([3, 2, 3, 6, 3, 10, 9, 3], 3, 4), ( [2, 11, 2, 2, 1], 2, 2))

    # for array, key, expected_length in data:
    #     a_ = array.copy()
    #     print(array)
    #     assert remove_key(a_, key) == expected_length
    #     print(array)
    print("Hey")
