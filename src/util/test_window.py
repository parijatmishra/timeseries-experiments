import pytest
import numpy as np
import pandas as pd
from window import simple_moving_average, median


def test_sma_illegalW_ndarray():
    with pytest.raises(AssertionError):
        simple_moving_average(np.array([1, 2, 3]), 4)


def test_sma_illegalW_series():
    with pytest.raises(AssertionError):
        simple_moving_average(pd.Series([1, 2, 3]), 4)


def test_sma_ndarray():
    x = np.array([1, 2, 3, 4, 5])
    y = simple_moving_average(x, 3)
    expect = np.array([np.NAN, np.NAN, (1+2+3)/3,
                      (2+3+4)/3, (3+4+5)/3], dtype=float)
    assert np.all(np.isclose(y, expect, equal_nan=True))


def test_median_array():
    x = np.array([1, 2, 10, 4, 5])
    y = median(x, 3)
    expect = np.array([np.NAN, np.NAN, 2, 4, 5], dtype=float)
    assert np.all(np.isclose(y, expect, equal_nan=True))
