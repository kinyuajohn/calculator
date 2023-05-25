import math
import pytest
from tkinter import *

from calc import click, add, sub, mul, div, mod, lcm, hcf, find_numbers


# Create a fixture for the tkinter root window
@pytest.fixture
def root():
    root = Tk()
    yield root
    root.destroy()


# Define test cases for the click function
@pytest.mark.parametrize(
    "value, ex, expected",
    [
        ("C", "123", "12"),
        ("CE", "123", ""),
        ("√", "16", 4),
        ("π", "", math.pi),
        ("cosθ", "90", 0),
        ("sinθ", "45", math.sqrt(2) / 2),
        ("tanθ", "45", 1),
        ("2π", "", 2 * math.pi),
        ("cosh", "0", 1),
        ("sinh", "0", 0),
        ("tanh", "0", 0),
        (chr(8731), "8", 2),
        ("x\u02b8", "2", "**"),
        ("x\u00B3", "2", 8),
        ("x\u00B2", "2", 4),
        ("ln", "2", math.log2(2)),
        ("deg", "180", 32768),
        ("rad", "180", math.radians(180)),
        ("e", "", math.e),
        ("log₁₀", "100", 2),
        ("x!", "5", math.factorial(5)),
        (chr(247), "10", "/"),
        ("=", "2 + 2", 4),
    ],
)
def test_click(value, ex, expected, root):
    entryField = Entry(root)
    entryField.insert(0, ex)
    click(value)
    assert entryField.get() == str(expected)


# Define test cases for the arithmetic operations
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 2, 3),
        (4, 4, 16),
        (10, 2, 5),
        (10, 3, 1),
    ],
)
def test_arithmetic_operations(a, b, expected):
    assert add(a, b) == expected
    assert sub(a, b) == expected
    assert mul(a, b) == expected
    assert div(a, b) == expected
    assert mod(a, b) == expected


# Define test cases for the helper functions
def test_find_numbers():
    text_list = ["1", "2", "3", "a", "b", "c"]
    expected = [1, 2, 3]
    assert find_numbers(text_list) == expected


# Additional test cases can be added as needed
