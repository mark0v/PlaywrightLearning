import pytest
from test_first import Task


@pytest.mark.important_test
def test_asdict():
    t_task = Task('Do it', 'Alex', True, 22)
    t_dict = t_task._asdict()
    expected = {'summary': 'Do it',
                'owner': 'Alex',
                'done': True,
                'id': 22}
    assert t_dict == expected
