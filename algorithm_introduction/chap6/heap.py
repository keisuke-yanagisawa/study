# coding: UTF-8 
class Heap(object):
    __array = None
    
    def __init__(self, array=[], ascending=True):
        self.__array = array
        self.__ascending = ascending
        self.build()

    def size(self):
        return len(self.__array)
    def show(self):
        print(self.__array)
    def swap(self, i, j):
        self.__array[i-1], self.__array[j-1] = self.__array[j-1], self.__array[i-1]
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        upper = i
        if l<=self.size() and (bool(self.getval(i) < self.getval(l)) ^ bool(self.__ascending)):
            upper = l
        if r<=self.size() and (bool(self.getval(upper) < self.getval(r)) ^ bool(self.__ascending)):
            upper = r
        if upper != i:
            self.swap(i, upper)
            self.heapify(upper)
            
    def build(self):
        for i in range(self.size()/2, 0, -1):
            self.heapify(i)
    def __pop(self, i):
        return self.__array.pop(i-1)
    def sort(self):
        ret = []
        for i in range(self.size(), 0, -1):
            self.swap(1, i)
            ret.append(self.__pop(i))
            self.heapify(1)
        return ret
  
    def getval(self, i):
        if i > len(self.__array) or i < 1:
            return None
        else:
            return self.__array[i-1]
    def setval(self, i, val):
        if i > len(self.__array) or i < 1:
            print("out of range.", i)
        else:
            self.__array[i-1] = val
  
    def parent(self, i):
        return (i-1)/2
    def left(self, i):
        return 2*i
    def right(self, i):
        return 2*i+1

if __name__ == "__main__":
    array = [1,7,2,8,4,6,3, 10, 20, 43]
    heap = Heap(array, ascending=True)
    print heap.sort()
