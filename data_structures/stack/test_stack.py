import pytest


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
