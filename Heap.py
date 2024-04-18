import sys
import Movie
class Heap:

    def __init__(self, m):
        self.max = m
        self.size = 0
        self.heap_arr = [m] * (self.size + 1)


    def getParent(self, child):
        return child // 2

    def getLeftChild(self, index):
        return 2 * index

    def getRightChild(self, index):
        return 1 + (2*index)

    def swap(self, a, b):
        pass

    def heapify(self, index):
        # build a heap in place
        pass

    def extractMax(self):
        pass
    def kthLargestElements(self, k):
        pass
