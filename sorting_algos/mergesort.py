def mergesort(unsorted_list):
    """Sort by dividing up halves and re-merging."""
    def _merge(left_half, right_half):
        """Re-merge."""
        merged = []
        left_index, right_index = 0, 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1
        merged += left_half[left_index:]
        merged += right_half[right_index:]
        return merged

    if len(unsorted_list) <= 1:
        return unsorted_list
    half = len(unsorted_list) // 2
    left, right = mergesort(unsorted_list[:half]), mergesort(unsorted_list[half:])
    return _merge(left, right)
