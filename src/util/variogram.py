import numpy as np
import pandas as pd
import statsmodels.api as sm


def variogram(x: np.ndarray, maxlag: int) -> np.ndarray:
    """Return a variogram of lags k=1,2,...,maxlag.

    x: a timeseries (numpy ndarray)

    returns: 1-dimensional ndarray of length `maxlag`.
      ret[0] = variogram(1)
      ...
      ret[maxlag-1] = variogram[maxlag]
    """
    def var(x, k):
        return np.var(x[k:]-x[:-k])

    ret = np.zeros((maxlag,), dtype=float)
    var_1 = var(x, 1)
    ret[0] = 1
    for k in range(2, maxlag+1):
        ret[k-1] = var(x, k) / var_1

    return ret
