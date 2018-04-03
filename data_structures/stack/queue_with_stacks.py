from stack import Stack as S

a = S([])
b = S([])


class Queue:
    """Queue data structure."""
    def enqueue(self, val):
        """Add to the queue."""
        a.push(val)
        return a.top.val

    def dequeue(self):
        """Remove from the queue."""
        if not b.top:
            while a.top:
                b.push(a.pop())
        return b.pop()
