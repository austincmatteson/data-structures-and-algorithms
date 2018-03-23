def largest_product(array):
    """Find largest product of adjacent in 2D array."""
    error(array)
    max = array[0][0] * array[0][1]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == len(array) - 1 and array[i][j] is array[i][-1]:
                break
            elif i == len(array) - 1:
                product1 = array[i][j] * array[i][j + 1]
            elif array[i][j] is array[i][-1]:
                product1 = array[i][j] * array[i - 1][j]
            else:
                product = array[i][j] * array[i][j + 1]
                product1 = array[i][j] * array[i + 1][j]
            if max < product:
                max = product
            if max < product1:
                max = product1
    return max


def error(arr):
    """Error handling of passing wrong parameters."""
    if type(arr) is not list:
        raise TypeError('Argument(s) invalid.')
    for i in range(len(arr)):
        if type(arr[i]) is not list:
            raise TypeError('Argument(s) invalid.')
        dimensions = len(arr[0])
        if dimensions != len(arr[i]):
            raise TypeError('Argument(s) invalid.')
        for j in range(len(arr[i])):
            if type(arr[i][j]) is not int:
                raise TypeError('Argument(s) invalid.')
