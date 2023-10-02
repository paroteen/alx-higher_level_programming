#!/usr/bin/python3
<<<<<<< HEAD
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
=======
"""
function that finds a peak in a list of unsorted
integers using binary sort
"""


def find_peak(list_of_integers):
    """
    function to find peak
    """
    l = len(list_of_integers)
    if l == 0:
        return
    half = l // 2
    if (half == l - 1 or list_of_integers[half] >=
        list_of_integers[half + 1]) and (half == 0 or list_of_integers[half] >=
                                         list_of_integers[half - 1]):
        return (list_of_integers[half])
    elif half != l - 1 and list_of_integers[half + 1] > list_of_integers[half]:
        return (find_peak(list_of_integers[half + 1:]))
    return (find_peak(list_of_integers[:half]))
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
