def next_center(center, min, max):
    """set center to correct new value"""
    true_center = ((max - min) // 2) + min
    if true_center != center:
        return true_center
    elif true_center == min:
        return max
    else:
        return min


def binary_search(arr, num):
    """return index of supplied value if exists"""
    min = 0
    max = len(arr) - 1
    center = next_center(-1, min, max)
    while max != min is True or max != center or min != center is True:
        center = next_center(center, min, max)
        if arr[center] == num:
            return center
        elif arr[center] > num:
            max = center
        else:
            min = center
    return -1
