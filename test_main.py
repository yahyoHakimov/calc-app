from main import add, divide, modulo
from utils import sqrt


def test_add():
    assert add(2, 3) == 5


def test_divide_by_zero():
    assert divide(5, 0) is None


def test_modulo():
    assert modulo(7, 3) == 1


def test_sqrt():
    assert sqrt(16) == 4