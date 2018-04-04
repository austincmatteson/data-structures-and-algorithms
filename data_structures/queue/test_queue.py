import pytest
from fifo_animal_shelter import Animal_Shelter


def test_empty_queue_has_no_front(empty_queue):
    """Check if empty."""
    assert empty_queue.front is None
    assert empty_queue.back is None


def test_insertion(empty_queue):
    """Check added correctly."""
    assert empty_queue.front is None
    assert empty_queue.enqueue(1).val == 1


def test_empty_val_on_enqueue(empty_queue):
    """Refuse adding nothing."""
    with pytest.raises(TypeError):
        empty_queue.enqueue()


def test_dequeue(small_queue):
    """Remove fifo."""
    assert small_queue.dequeue() == 1
    assert small_queue.dequeue() == 2
    assert small_queue.dequeue() == 3
    assert small_queue.dequeue() == 4
    assert small_queue.dequeue() == 5
    assert small_queue.dequeue() is None


def test_empty_dequeue(empty_queue):
    """Remove nothing."""
    assert empty_queue.dequeue() is None


def test_animal_enqueue():
    """Insert only cats and dogs."""
    a = Animal_Shelter()
    assert a.enqueue('dog') == 'dog'
    assert a.enqueue('cat') == 'cat'
    with pytest.raises(TypeError):
        a.enqueue('bird')


def test_animal_dequeue():
    """Remove by preference or first by default."""
    a = Animal_Shelter()
    a.enqueue('dog') == 'dog'
    a.enqueue('cat') == 'cat'
    a.enqueue('cat') == 'cat'
    a.enqueue('cat') == 'cat'
    a.enqueue('dog') == 'dog'
    assert a.dequeue() == 'dog'
    assert a.dequeue() == 'cat'
    assert a.dequeue('dog') == 'dog'
    assert a.dequeue('cat') == 'cat'
    assert a.dequeue() == 'cat'
    assert a.dequeue() is None
