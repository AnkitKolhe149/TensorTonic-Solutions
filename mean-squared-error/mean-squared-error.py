import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    
    mean = 0
    for i in range(len(y_pred)):
        mean += (y_pred[i] - y_true[i]) ** 2

    return mean / len(y_pred)
