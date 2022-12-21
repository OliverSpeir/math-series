import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


def test_fibonacci_3():
    """
    tests the fibonacci function at n = 3
    """
    actual = fibonacci(3)
    expect = 2
    assert actual == expect


def test_fibonacci_0():
    """
    tests the fibonacci function at n = 0
    """
    actual = fibonacci(0)
    expect = 0
    assert actual == expect


def test_lucas_3():
    """
    tests the lucas function at n = 3
    """
    actual = lucas(3)
    expect = 4
    assert actual == expect


def test_lucas_0():
    """
    tests the lucas function at n = 0
    """
    actual = lucas(0)
    expect = 2
    assert actual == expect


def test_sum_series_3():
    """
    tests the sum_series function at n = 3 without optional args (expected fibonacci like behavior)
    """
    actual = sum_series(3)
    expect = 2
    assert actual == expect


def test_sum_series_0():
    """
    tests the sum_series function at n = 0 without optional args (expected fibonacci like behavior)
    """
    actual = sum_series(0)
    expect = 0
    assert actual == expect


def test_sum_series_with_options_at_3():
    """
    tests the sum_series function at n = 3 without optional args (expected lucas like behavior)
    """
    actual = sum_series(3, 2, 1)
    expect = 4
    assert actual == expect


def test_sum_series_with_options_at_0():
    """
    tests the sum_series function at n = 3 without optional args (expected lucas like behavior)
    """
    actual = sum_series(0, 2, 1)
    expect = 2
    assert actual == expect
