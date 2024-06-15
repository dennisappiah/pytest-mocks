import pytest

from student import Student


# using pytest to create class objects (pytest objects) and passing it as function parameter
@pytest.fixture
def default_student():
    return Student("dennis", "appiah", "english", 12)


def test_student_initialisation(default_student):
    assert default_student.firstname == "dennis"
    assert default_student.lastname == "appiah"
    assert default_student.major == "english"
    assert default_student.years == 12
