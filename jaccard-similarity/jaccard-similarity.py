import numpy as np
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a=set(set_a)
    set_b=set(set_b)
    num=set_a.intersection(set_b)
    den=set_a.union(set_b)
    if(len(den)==0):
        return 0
    return len(num)/len(den)