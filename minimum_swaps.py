def minimum_swaps(arr):
    """
    two of the functions minimum_swaps take shuffled lists of consecutive ints from 1 to n, and find the minimum swaps
    needed to be done between members of the list to be sorted, and return it.
    :param arr: list of ints
    :return: int
    """
    swaps = 0
    swaps_in_a_round = 1
    while swaps_in_a_round:
        swaps_in_a_round = 0
        for i, number in enumerate(arr):
            if number != i+1:
                arr[i], arr[number-1] = arr[number-1], arr[i]
                swaps += 1
                swaps_in_a_round += 1
    return swaps


def minimum_swaps(arr):
    swaps = 0
    for i, number in enumerate(arr):
        if number != i+1:
            j = arr[i:].index(i+1) + i
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    return swaps
