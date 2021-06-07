from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_one_fibonacci():
    expected = 5
    actual = fibonacci(5)
    assert expected == actual

def test_two_fibonacci():
    expected = 13
    actual = fibonacci(7)
    assert expected == actual

def test_three_fibonacci():
    expected = "Put an intger"
    actual = fibonacci("sss")
    assert expected == actual

def test_one_lucas():
    expected = 11
    actual = lucas(5)
    assert expected == actual

def test_two_lucas():
    expected = 29
    actual = lucas(7)
    assert expected == actual

def test_three_lucas():
    expected = "Put an intger"
    actual = lucas("sss")
    assert expected == actual

def test_one_sum_series():
    expected = 5
    actual = sum_series(5)
    assert expected == actual

def test_two_sum_series():
    expected = 18
    actual = sum_series(4,3,4)
    assert expected == actual

def test_three_sum_series():
    expected = 47
    actual = sum_series(6,3,4)
    assert expected == actual

def test_four_sum_series():
    expected = "Put an intger"
    actual = sum_series("sss")
    assert expected == actual

def test_four_sum_series():
    expected = "Put an intger"
    actual = sum_series("sss",4,"sad")
    assert expected == actual