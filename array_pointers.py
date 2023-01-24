#!/usr/bin/env python3
import math


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


def triple_sum_to_zero(numbers):
    """
    Given an array of unsorted numbers, find all unique
    triplets in it that add up to zero.
    """
    # Brute force:
    # iterate over all permutations of 3 index in the array
    # check if they sum zero and store the value of each index (as tuples)
    # in a set.
    # if we always order the values of the index before adding them to set
    # it will discard any duplications
    #
    # result = set()
    # size = len(numbers)
    # for i in range(size):
    #     for j in range(i + 1, size):
    #         for k in range(j + 1, size):
    #             if numbers[i] + numbers[j] + numbers[k] == 0:
    #                 result.add(tuple(sorted([numbers[i], numbers[j], numbers[k]])))

    # return list(result)

    # for any 2 index, do we have a 3rd index whose
    # value equals the inverse of their sum?
    sorted_numbers = sorted(numbers)
    results = []

    for i in range(len(numbers)):
        if i > 0 and sorted_numbers[i] == sorted_numbers[i - 1]:
            continue
        results += _search_pairs(sorted_numbers, i, -sorted_numbers[i])
    return results


def _search_pairs(nums, left, target_sum):
    triplets = []
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]
        if current == target_sum:
            triplets.append([-target_sum, nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right + 1] == nums[right]:
                right -= 1
        elif current < target_sum:
            left += 1
        else:
            right -= 1
    return triplets


def triple_sum_close_to_target(numbers, target):
    """
    Given an array of unsorted numbers and a target number, find a
    triplet in the array whose sum is as close to the target
    number as possible, return the sum of the triplet.
    If there are more than one such triplet, return the
    sum of the triplet with the smallest sum.
    """
    sorted_nums = sorted(numbers)
    best_diff = math.inf
    for left_index, n in enumerate(sorted_nums):
        if left_index >= len(sorted_nums) - 2:
            # We can not build a triple with the last 2 elements of the array
            continue

        left = left_index + 1
        right = len(sorted_nums) - 1
        while left < right:
            current_sum = sum(
                (sorted_nums[left_index], sorted_nums[left], sorted_nums[right])
            )
            current_diff = target - current_sum

            if current_diff == 0:
                return target

            if abs(current_diff) < abs(best_diff) or (
                abs(current_diff) == abs(best_diff) and current_sum < target - best_diff
            ):
                best_diff = current_diff

            if current_diff > 0:
                left += 1
            else:
                right -= 1

    return target - best_diff


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

    # data = [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]), ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9])]
    # for array, result in data:
    #     assert same_items(square_sorted(array), result)

    # data = [[-3, 0, 1, 2, -1, 1, -2], [-5, 2, -1, -2, 3]]
    # for array in data:
    #     print(triple_sum_to_zero(array))

    data = [
        ([-2, 0, 1, 2], 2, 1),
        ([-3, -1, 1, 2], 1, 0),
        ([1, 0, 1, 1], 100, 3),
        ([0, 0, 1, 1, 2, 6], 5, 4),
    ]
    for array, target, result in data:
        assert triple_sum_close_to_target(array, target) == result
