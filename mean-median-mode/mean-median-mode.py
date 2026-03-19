import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    mean=float(np.mean(x))
    median=float(np.median(x))
    freq = Counter(x)
    mode = float(max(freq, key=freq.get))
    return mean,median,mode