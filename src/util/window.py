import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d, median_filter


def simple_moving_average(x: np.ndarray, W: int) -> np.ndarray:
    """Given an input array, return a new array containing the simple
    moving average over a window size W. The returned array has the
    same number of elements as the input, but the first W-1 elements
    are set to np.NAN (float).

    params:
        x: a one-dimensional numpy ndarray, or a pandas Series
        W: the size of the moving average window. W must be <= len(x).
    returns:
        A numpy ndarray of shape (1, N), or a pandas Series of length N.
        The `dtype` of the elements is float.
        The first W-1 values are set to numpy.NAN.
        If x is a Series, the return value will be a Series with the same index as x.
    errors:
        Raises an AssertionError is W > len(x)
    """

    assert W <= len(x)

    N = len(x)
    Leave = int(W/2) if (W % 2 == 0) else int((W-1)/2)
    Take = N - W + 1
    Prefix = np.full(W-1, np.NAN, dtype=float)

    y = uniform_filter1d(x, W, mode='constant')
    z = np.concatenate([Prefix, y[Leave:][:Take]])
    return z


def median(x: np.ndarray, W: int) -> np.ndarray:
    """Given an input array, return a new array containing the simple
    moving average over a window size W. The returned array has the
    same number of elements as the input, but the first W-1 elements
    are set to np.NAN (float).

    params:
        x: a one-dimensional numpy ndarray, or a pandas Series
        W: the size of the moving average window. W must be <= len(x).
    returns:
        A numpy ndarray of shape (1, N), or a pandas Series of length N.
        The `dtype` of the elements is float.
        The first W-1 values are set to numpy.NAN.
        If x is a Series, the return value will be a Series with the same index as x.
    errors:
        Raises an AssertionError is W > len(x)
    """

    assert W <= len(x)

    N = len(x)
    Leave = int(W/2) if (W % 2 == 0) else int((W-1)/2)
    Take = N - W + 1
    Prefix = np.full(W-1, np.NAN, dtype=float)

    y = median_filter(x, W, mode='constant')
    z = np.concatenate([Prefix, y[Leave:][:Take]])
    return z
