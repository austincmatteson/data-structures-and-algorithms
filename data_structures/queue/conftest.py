import pytest
from queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    return q


@pytest.fixture
def large_queue():
    q = Queue()
    for num in range(1000):
        q.enqueue(num)
    return q
