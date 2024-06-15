import pytest


def test_equal_not_equal():
    assert 3 == 3
    assert 3 != 1


def test_is_instance():
    assert isinstance("this is a string", str)
    assert not isinstance("10", int)


def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False


def test_type():
    assert type("hello" is str)


def test_list():
    numbers = [1, 2, 3, 4, 5]
    anylist = [False, False]

    assert 1 in numbers
    assert 7 not in numbers
    assert all(numbers)
    assert not any(anylist)


# parameterizing tests
@pytest.mark.parametrize("a, b, final", [(2, 4, 6), (3, 5, 8)])
def test_add(a, b, final):
    assert a + b == final
