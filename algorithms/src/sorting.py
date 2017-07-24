"""
Common sorting algorithms.
"""

def quicksort(u_list):
    """
    Implements a quicksort algorithm.
    ---------------------------------
    Inputs:
        u_list : Unsorted List
    Outputs:
        u_list : Sorted List
    """

    less = []
    equal = []
    greater = []
    if len(u_list) > 1:
        pivot = u_list[0]
        for x in u_list:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return u_list
