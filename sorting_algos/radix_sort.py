def radix(unsorted_list):
    """Sort via radix."""
    def _rad(sort_list, it):
        """Sorting."""
        buckets = [[] for _ in range(10)]
        for each in sort_list:
            i = (each // (10 ** it)) % 10
            buckets[i].append(each)
        sort_list = []
        for bucket in buckets:
            for each in bucket:
                sort_list.append(each)
        return sort_list
    if len(unsorted_list) <= 1:
        return unsorted_list
    max_val = abs(max(unsorted_list, key=abs))
    iterations = 0
    while (10 ** iterations) <= max_val:
        unsorted_list = _rad(unsorted_list, iterations)
        iterations += 1
    return unsorted_list
