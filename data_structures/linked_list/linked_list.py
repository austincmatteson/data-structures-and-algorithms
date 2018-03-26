from node import Node


class LinkedList:
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            print('Not an iterable')

    def __str__(self):
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        start = self.head
        search = self.head._next
        try:
            while start is not None:
                if start.val == val:
                    return True
                else:
                    start = search
                    search = start._next
        except AttributeError:
            return False
