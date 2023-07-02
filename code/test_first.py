from collections import namedtuple


def test_pass():
    assert (1, 2, 3) == (1, 2, 3)


def test_fail():
    assert (1, 2, 3) == (1, 2, 4)


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    task1 = Task()
    expected = Task(None, None, False, None)
    assert task1 == expected


def test_defaults_fail():
    task1 = Task()
    expected = Task(None, None, True, None)
    assert task1 == expected


def test_member_access():
    t = Task('buy milk', id=12)
    assert t.summary == 'buy milk'
    assert t.id == 12
    assert (t.owner, t.done) == (None, False)
