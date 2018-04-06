def towers_of_hanoi(n):
    """Solve towers of hanoi game for any number of discs."""
    a = ([], 'A')
    b = ([], 'B')
    c = ([], 'C')
    count = 0
    for i in reversed(range(n)):
        a[0].append(i + 1)
    count = move(n, a, b, c, count)
    return a[0], b[0], c[0], count


def move(n, start, temp, end, count):
    """Move discs around pegs."""
    if n > 0:
        count = move(n - 1, start, end, temp, count)
        if start:
            end[0].append(start[0].pop())
            print('Disk {} moved from {} to {}'.format(n, start[1], end[1]))
            count += 1
        count = move(n - 1, temp, start, end, count)
    return count
