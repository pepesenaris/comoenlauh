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


def square_sorted(sorted_array):
    """
    Given a sorted array, create a new array containing squares of all
    the numbers of the input array in the sorted order.
    """
    # Trivial O(n log n) + O(n) = O(n log n)
    # return sorted([n**2 for n in sorted_array])

    left = 0
    right = len(sorted_array) - 1
    squares = [None] * len(sorted_array)
    index = right
    # We start with the last element of the array
    # and continue in descending order always getting the
    # new bigger square

    while left <= right:
        p_left = sorted_array[left] ** 2
        p_right = sorted_array[right] ** 2

        if p_left > p_right:
            squares[index] = p_left
            left += 1
        else:
            squares[index] = p_right
            right -= 1
        index -= 1

    return squares


def same_items(array1, array2):
    s1 = set(array1)
    s2 = set(array2)

    return (
        len(array1) == len(array)
        and all([n in s2 for n in array1])
        and all([n in s1 for n in array2])
    )


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

    data = [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]), ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9])]
    for array, result in data:
        assert same_items(square_sorted(array), result)
