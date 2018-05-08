def selection_sort(unsorted_list):
    """Sort via selection algorithm."""
    if len(unsorted_list) <= 1:
        return unsorted_list
    for index in range(len(unsorted_list)):
        lowest_number = index
        for i in range(index, len(unsorted_list)):
            if unsorted_list[lowest_number] > unsorted_list[i]:
                lowest_number = i
        unsorted_list[index], unsorted_list[lowest_number] = unsorted_list[lowest_number], unsorted_list[index]
    return unsorted_list
