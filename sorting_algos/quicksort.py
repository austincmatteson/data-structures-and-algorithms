from random import randint


def quick_sort(array):
    """Sort quickly."""
    def _partition(partial_list, start, end):
        """Swap correctly."""
        rand = randint(start, end)
        partial_list[end], partial_list[rand] = partial_list[rand], partial_list[end]
        pivot = start
        for i in range(start, end):
            if partial_list[i] < partial_list[end]:
                partial_list[i], partial_list[pivot] = partial_list[pivot], partial_list[i]
                pivot += 1
        partial_list[pivot], partial_list[end] = partial_list[end], partial_list[pivot]
        return pivot

    def _sort(unsorted_list, start, end):
        """Split correctly."""
        if start < end:
            pivot = _partition(unsorted_list, start, end)
            _sort(unsorted_list, start, pivot - 1)
            _sort(unsorted_list, pivot + 1, end)
        return unsorted_list
    start = 0
    end = len(array) - 1
    return _sort(array, start, end)

# def quick_sort(l):
#     """."""
#     less = []
#     more = []
#     equal = []
#     if len(l) > 1:
#         temp = l[0]
#         for i in l:
#             if i < temp:
#                 less.append(i)
#             elif i > temp:
#                 more.append(i)
#             else:
#                 equal.append(i)
#         return quick_sort(less) + equal + quick_sort(more)
#     else:
#         return l
