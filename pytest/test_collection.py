import pytest
from collections import namedtuple

Student = namedtuple('student', ['Name', 'Age', 'University'])
Student.__new__.__defaults__ = (None, None, None)

def test_defaults():
    """ Using no parameters should invoke defaults """
    s1 = Student()
    s2 = Student(None, None, None)
    assert s1 == s2

def test_member_access():
    """ Check field functionality of namedtuple """
    s = Student('Juan', 23)
    assert s.Name == 'Juan'
    assert s.Age == 23 
    assert s.University == None