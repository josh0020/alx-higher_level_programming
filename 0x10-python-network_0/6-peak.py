#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak integer found in the list or None if the list is empty.

    Note:
        There may be more than one peak in the list.

    Complexity:
        This algorithm has a time complexity of O(log(n)).
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
