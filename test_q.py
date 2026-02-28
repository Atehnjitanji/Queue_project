from q import *

def test_empty():
    empty = Queue()
    assert empty.is_empty()

def test_add():
    q = Queue()
    q.add("A")
    assert q.head
