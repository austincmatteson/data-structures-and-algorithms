import pytest
from queue_with_stacks import Queue
from multi_bracket_validation import multi_bracket_validation as mbv


def test_empty_stack_has_no_top(empty_stack):
    """Check is empty."""
    assert empty_stack.top is None


def test_insertion(empty_stack):
    """Insert correctly."""
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    """Refuse inserting nothing."""
    with pytest.raises(TypeError):
        empty_stack.push()


def test_pop(small_stack):
    """Remove lifo."""
    assert small_stack.pop() == 5
    assert small_stack.pop() == 4
    assert small_stack.pop() == 3
    assert small_stack.pop() == 2
    assert small_stack.pop() == 1
    assert small_stack.pop() is None


def test_empty_pop(empty_stack):
    """Remove nothing when empty."""
    assert empty_stack.pop() is None


def test_peek(large_stack, empty_stack):
    """View top."""
    assert large_stack.peek() == 999
    large_stack.pop()
    assert large_stack.peek() == 998
    large_stack.push(1000)
    assert large_stack.peek() == 1000
    with pytest.raises(AttributeError):
        empty_stack.peek()


def test_qstack_add():
    """Enqueue using stacks."""
    q = Queue()
    assert q.enqueue(1) == 1
    assert q.enqueue(2) == 2
    assert q.enqueue(3) == 3
    assert q.enqueue(4) == 4


def test_qstack_remove():
    """Dequeue using stacks."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4


def test_bracket_none():
    """Test no brackets."""
    assert mbv(' ') is True


def test_bracket_true():
    """Test balanced."""
    assert mbv('[]') is True
    assert mbv('{}') is True
    assert mbv('()') is True
    assert mbv('{[()]}') is True
    assert mbv('{dasd[dasd(asdsa)dsad]dasd}') is True


def test_bracket_false():
    """Test unbalanced."""
    assert mbv('(') is False
    assert mbv('][') is False
    assert mbv('()()()(') is False
    assert mbv('{[}]') is False
