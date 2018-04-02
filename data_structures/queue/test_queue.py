import pytest


def test_empty_queue_has_no_front(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None


def test_insertion(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.enqueue(1).val == 1


def test_empty_val_on_enqueue(empty_queue):
    with pytest.raises(TypeError):
        empty_queue.enqueue()


def test_dequeue(small_queue):
    assert small_queue.dequeue() == 1
    assert small_queue.dequeue() == 2
    assert small_queue.dequeue() == 3
    assert small_queue.dequeue() == 4
    assert small_queue.dequeue() == 5
    assert small_queue.dequeue() is None


def test_empty_dequeue(empty_queue):
    assert empty_queue.dequeue() is None
