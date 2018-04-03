import pytest
from queue_with_stacks import Queue


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_insertion(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push()


def test_pop(small_stack):
    assert small_stack.pop() == 5
    assert small_stack.pop() == 4
    assert small_stack.pop() == 3
    assert small_stack.pop() == 2
    assert small_stack.pop() == 1
    assert small_stack.pop() is None


def test_empty_pop(empty_stack):
    assert empty_stack.pop() is None


def test_peek(large_stack, empty_stack):
    assert large_stack.peek() == 999
    large_stack.pop()
    assert large_stack.peek() == 998
    large_stack.push(1000)
    assert large_stack.peek() == 1000
    with pytest.raises(AttributeError):
        empty_stack.peek()


def test_qstack_add():
    q = Queue()
    assert q.enqueue(1) == 1
    assert q.enqueue(2) == 2
    assert q.enqueue(3) == 3
    assert q.enqueue(4) == 4


def test_qstack_remove():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
