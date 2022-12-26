import pytest

from day_25 import snafu_to_decimal, decimal_to_snafu


testdata = [
    ("1", 1),
    ("2", 2),
    ("1=", 3),
    ("1-", 4),
    ("10", 5),
    ("11", 6),
    ("12", 7),
    ("2=", 8),
    ("2-", 9),
    ("20", 10),
    ("1=0", 15),
    ("1-0", 20),
    ("1=11-2", 2022),
    ("1-0---0", 12345),
    ("1121-1110-1=0", 314159265),
]


@pytest.mark.parametrize("snafu, decimal", testdata)
def test_snafu_to_decimal(snafu, decimal):
    assert snafu_to_decimal(snafu) == decimal


@pytest.mark.parametrize("snafu, decimal", testdata)
def test_decimal_to_snafu(snafu, decimal):
    assert decimal_to_snafu(decimal) == snafu
