from hash_table import HashTable as HT
from repeated_word import repeated_word as rw
import pytest


def test_hash_size():
    """."""
    ht = HT()
    assert ht.max_size == 1024


def test_hash_size2():
    """."""
    ht = HT(2)
    assert ht.max_size == 2


def test_hash_size_fail():
    """."""
    with pytest.raises(TypeError):
        assert HT('zero')


def test_set_empty():
    """."""
    ht = HT()
    assert ht.set('hello', 'world') == {'hello': 'world'}


def test_set_into_existing(hash_test):
    """."""
    assert hash_test.set('sup', 'bro') == {'sup': 'bro'}


def test_set_fail(hash_test):
    """."""
    with pytest.raises(TypeError):
        assert hash_test.set(1, 1)


def test_get(hash_test):
    """."""
    assert hash_test.get('meow') == 1
    assert hash_test.get('woof') == 2
    assert hash_test.get('blammo') == 3


def test_get_overwrite(hash_test):
    """."""
    hash_test.set('meow', 2)
    assert hash_test.get('meow') == 2


def test_get_key_does_not_exist(hash_test):
    """."""
    assert hash_test.get('fizzbuzz') is None


def test_remove_empty():
    """."""
    ht = HT()
    assert ht.remove('hi') is None


def test_remove(hash_test):
    """."""
    assert hash_test.remove('meow') == {'meow':  1}


def test_remove_multi(hash_test):
    """."""
    hash_test.set('meow', 2)
    hash_test.set('meow', 3)
    assert hash_test.remove('meow') == {'meow': 3}
    assert hash_test.remove('meow') == {'meow': 2}
    assert hash_test.remove('meow') == {'meow': 1}
    assert hash_test.remove('meow') is None


def test_repeated_word():
    """."""
    assert rw(
        'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only') == 'it'


def test_repeated_word_none():
    """."""
    assert rw('It was the') is None


def test_repeated_word_fail():
    """."""
    with pytest.raises(AttributeError):
        assert rw(1)
