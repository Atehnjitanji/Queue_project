from q import *

def test_empty():
    empty = Queue()
    assert empty.is_empty()

def test_add():
    q = Queue()
    q.add("A")
    assert q.head

def test_size():
    q = Queue()
    q.add("A")
    q.add("B")
    q.add("C")
    q.add("D")
    q.add("E")
    assert q.size == 5

def test_pop():
    q = Queue()
    q.add("B")
    q.add("A")
    assert q.pop_left() == "B"
