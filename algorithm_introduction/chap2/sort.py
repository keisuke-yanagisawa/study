# coding: UTF-8 
import sys
from numpy import random

LENGTH=int(sys.argv[1])

def insertionSort(alist):
    for i in range(len(alist)):
        key = alist[i]
        j = i-1
        while j>=0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key
    return alist

def __merge(left, right):
    newlist = []
    while(len(left) != 0 and len(right) != 0):
        if(left[0] <= right[0]):
            newlist.append(left.pop(0))
        else:
            newlist.append(right.pop(0))

    if len(left) != 0:
        newlist.extend(left)
    elif len(right) != 0:
        newlist.extend(right)

    return newlist
    
def mergeSort(alist):
    if len(alist) <=1:
        return alist;

    left  = mergeSort(alist[:len(alist)/2])
    right = mergeSort(alist[len(alist)/2:])
    return __merge(left, right)

if __name__ == '__main__':
    alist=list(random.choice(LENGTH, LENGTH, replace=False))
    #insertionSort(alist)
    print mergeSort(alist)

