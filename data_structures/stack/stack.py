from node import Node


class Stack:
    """Stack data structure."""
    def __init__(self, iter=[]):
        """Intialize stack."""
        self.top = None
        self._size = 0

        try:
            for item in reversed(iter):
                self.push(item)
        except TypeError:
            raise TypeError('Please pass an iterable.')

    def __str__(self):
        """Return current top value."""
        return '<top> => {}'.format(self.top.val)

    def __len__(self):
        """Return current stack length."""
        return self._size

    def push(self, val):
        """Push new value onto stack."""
        self.top = Node(val, self.top)
        self._size += 1
        return self.top

    def pop(self):
        """Pop value from top of stack."""
        if self._size == 0:
            print('Stack is empty.')
        else:
            popped = self.top
            self.top = self.top._next
            self._size -= 1
            return popped.val

    def peek(self):
        """Return current top of stack."""
        return self.top.val
