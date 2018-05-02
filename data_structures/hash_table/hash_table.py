from functools import reduce
from linked_list import LinkedList as LL


class HashTable:
    """Hash table."""

    def __init__(self, max_size=1024):
        """Initialize."""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def _hash_key(self, key):
        """Hash map logic."""
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """Insert into hash table."""
        return self.buckets[self._hash_key(key)].insert({key: val})

    def get(self, key, filter=None):
        """Get all values at key."""
        current = self.buckets[self._hash_key(key)].head
        values = []
        while current:
            if key in current.val.keys():
                values.append(current.val[key])
            current = current._next
        return values

    def remove(self, key):
        """Remove last value of key."""
        start = self.buckets[self._hash_key(key)]
        current = start.head
        while current:
            removed, current = current.val, current._next
            start.head = current
            return removed
