# coding: UTF-8 

import numpy as np

def dac(alist):

    localmax = -np.inf
    localmin = np.inf
    score = 0

    if len(alist) == 1:
        localmax = max(alist)
        localmin = min(alist)
        score = localmax - localmin
        return localmax, localmin, score
    elif len(alist) == 0:
        return localmax, localmin, 0

    left  = dac(alist[:len(alist)/2])
    right = dac(alist[len(alist)/2:])

    score = left[2] if left[2]>right[2] else right[2]
    mid_score = right[0] - left[1]
    score = score if score > mid_score else mid_score

    localmax = max([left[0], right[0]])
    localmin = min([left[1], right[1]])

    return localmax, localmin, score

if __name__ == '__main__':
    alist = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    print dac(alist)
