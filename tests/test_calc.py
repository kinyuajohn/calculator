import pytest

from calc import add, sub, mul, div, mod, lcm, hcf


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(3, 5) == -2
    assert sub(0, 0) == 0


def test_mul():
    assert mul(2, 3) == 6
    assert mul(-2, 3) == -6
    assert mul(0, 5) == 0


def test_div():
    assert div(6, 3) == 2
    assert div(10, 2) == 5
    assert div(5, 0) == "Error: Division by zero"


def test_mod():
    assert mod(7, 3) == 1
    assert mod(10, 5) == 0
    assert mod(8, 2) == 0


def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(9, 12) == 36
    assert lcm(0, 5) == 0


def test_hcf():
    assert hcf(4, 6) == 2
    assert hcf(9, 12) == 3
    assert hcf(0, 5) == 5
