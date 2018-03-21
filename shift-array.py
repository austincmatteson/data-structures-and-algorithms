def insertShiftArray(arr, num):
    output = [0] * (len(arr) + 1)
    middle = (len(arr) + len(arr) % 2) // 2
    for i in range(len(output)):
        if i < middle:
            output[i] = arr[i]
        elif i == middle:
            output[i] = num
        else:
            output[i] = arr[i - 1]
    return output
