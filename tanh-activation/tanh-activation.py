import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x=np.array(x)
    return (pow(np.e,x)-pow(np.e,-x))/(pow(np.e,x)+pow(np.e,-x))