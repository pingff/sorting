#!/bin/python3


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    i, j = 0, 0
    res = []
    while i < len(xs) and j < len(ys):
        if cmp(xs[i], ys[j]) == -1:
            res.append(xs[i])
            i += 1
        else:
            res.append(ys[j])
            j += 1
    res.extend(xs[i:])
    res.extend(ys[j:])
    return res


def merge_sorted(xs, cmp=cmp_standard):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2
    left = xs[:mid]
    right = xs[mid:]

    left = merge_sorted(left, cmp)
    right = merge_sorted(right, cmp)

    return merge(left, right, cmp)


def merge(left, right, cmp):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
    left (list): The left sorted list.
    right (list): The right sorted list.
    cmp (function): The comparison function to be used for sorting.

    Returns:
    list: A new sorted list containing all elements of the input lists.
    """
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if cmp(left[i], right[j]) <= 0:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def quick_sorted(xs, cmp=cmp_standard):
    if len(xs) <= 1:
        return xs

    pivot = xs[0]
    lt, eq, gt = partition(xs, pivot, cmp)

    lt = quick_sorted(lt, cmp)
    gt = quick_sorted(gt, cmp)

    return lt + eq + gt


def partition(xs, pivot, cmp):
    """
    Partitions the input list xs into three sublists based on a pivot value.

    Parameters:
    xs (list): The input list to be partitioned.
    pivot (any): The pivot value to partition around.
    cmp (function): The comparison function to be used for sorting.

    Returns:
    tuple: A tuple containing three lists:
           - lt: a list of elements less than the pivot
           - eq: a list of elements equal to the pivot
           - gt: a list of elements greater than the pivot
    """
    lt, eq, gt = [], [], []
    for x in xs:
        if cmp(x, pivot) < 0:
            lt.append(x)
        elif cmp(x, pivot) == 0:
            eq.append(x)
        else:
            gt.append(x)

    return lt, eq, gt


def quick_sort(xs, cmp=cmp_standard):
    def partition_lomuto(xs, lo, hi):
        pivot = xs[hi]
        i = lo - 1
        for j in range(lo, hi):
            if cmp(xs[j], pivot) < 0:
                i += 1
                xs[i], xs[j] = xs[j], xs[i]
        xs[i + 1], xs[hi] = xs[hi], xs[i + 1]
        return i + 1

    def quicksort_helper(xs, lo, hi):
        if lo < hi:
            p = partition_lomuto(xs, lo, hi)
            quicksort_helper(xs, lo, p - 1)
            quicksort_helper(xs, p + 1, hi)

    quicksort_helper(xs, 0, len(xs) - 1)
