# context of test_sample.py
def func(x):
    return x + 1


def fun(x):
    return x * x


def test_answer():
    assert func(3) == 4


def test_square():
    assert fun(4) == 16
