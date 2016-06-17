# coding: UTF-8
def quicksort(alist, p, r):
    if p < r:
        q = partition(alist, p, r) 
        quicksort(alist, p, q-1)
        quicksort(alist, q+1, r)

def partition(alist, p, r):
    x = alist[r]
    i = p
    for j in range(p, r):
        if x > alist[j]:
            alist[i], alist[j] = alist[j], alist[i]
            i+=1
    alist[i], alist[r] = alist[r], alist[i]
    return i

if __name__ == "__main__":
    alist = [2, 8, 7, 1, 3, 5, 6, 4]
    quicksort(alist, 0, 7)
    print alist
